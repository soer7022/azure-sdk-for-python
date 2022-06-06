# The MIT License (MIT)
# Copyright (c) 2021 Microsoft Corporation

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""Internal class for multi execution context aggregator implementation in the Azure Cosmos database service.
"""

from azure.cosmos._execution_context.aio.base_execution_context import _QueryExecutionContextBase
from azure.cosmos._execution_context.aio import document_producer, _queue_async_helper
from azure.cosmos._routing import routing_range
from azure.cosmos import exceptions

# pylint: disable=protected-access


class _MultiExecutionContextAggregator(_QueryExecutionContextBase):
    """This class is capable of queries which requires rewriting based on
    backend's returned query execution info.

    This class maintains the execution context for each partition key range
    and aggregates the corresponding results from each execution context.

    When handling an orderby query, _MultiExecutionContextAggregator
    instantiates one instance of DocumentProducer per target partition key range
    and aggregates the result of each.
    """

    # TODO improvement: this class needs to be parallelized

    class PriorityQueue:
        """Provides a Priority Queue abstraction data structure"""

        def __init__(self):
            self._heap = []

        async def pop_async(self, document_producer_comparator):
            return await _queue_async_helper.heap_pop(self._heap, document_producer_comparator)

        async def push_async(self, item, document_producer_comparator):
            await _queue_async_helper.heap_push(self._heap, item, document_producer_comparator)

        def peek(self):
            return self._heap[0]

        def size(self):
            return len(self._heap)

    def __init__(self, client, resource_link, query, options, partitioned_query_ex_info):
        super(_MultiExecutionContextAggregator, self).__init__(client, options)

        # use the routing provider in the client
        self._routing_provider = client._routing_map_provider
        self._client = client
        self._resource_link = resource_link
        self._query = query
        self._partitioned_query_ex_info = partitioned_query_ex_info
        self._sort_orders = partitioned_query_ex_info.get_order_by()

        if self._sort_orders:
            self._document_producer_comparator = document_producer._OrderByDocumentProducerComparator(self._sort_orders)
        else:
            self._document_producer_comparator = document_producer._PartitionKeyRangeDocumentProducerComparator()

        self._orderByPQ = _MultiExecutionContextAggregator.PriorityQueue()

    async def __anext__(self):
        """Returns the next result

        :return: The next result.
        :rtype: dict
        :raises StopIteration: If no more result is left.
        """
        if self._orderByPQ.size() > 0:

            targetRangeExContext = await self._orderByPQ.pop_async(self._document_producer_comparator)
            res = await targetRangeExContext.__anext__()

            try:
                # TODO: we can also use more_itertools.peekable to be more python friendly
                await targetRangeExContext.peek()
                await self._orderByPQ.push_async(targetRangeExContext, self._document_producer_comparator)

            except StopAsyncIteration:
                pass

            return res
        raise StopAsyncIteration

    async def fetch_next_block(self):

        raise NotImplementedError("You should use pipeline's fetch_next_block.")

    async def _repair_document_producer(self):
        """Repairs the document producer context by using the re-initialized routing map provider in the client,
        which loads in a refreshed partition key range cache to re-create the partition key ranges.
        After loading this new cache, the document producers get re-created with the new valid ranges.
        """
        # refresh the routing provider to get the newly initialized one post-refresh
        self._routing_provider = self._client._routing_map_provider
        # will be a list of (partition_min, partition_max) tuples
        targetPartitionRanges = await self._get_target_partition_key_range()

        targetPartitionQueryExecutionContextList = []
        for partitionTargetRange in targetPartitionRanges:
            # create and add the child execution context for the target range
            targetPartitionQueryExecutionContextList.append(
                self._createTargetPartitionQueryExecutionContext(partitionTargetRange)
            )

        for targetQueryExContext in targetPartitionQueryExecutionContextList:
            try:
                # TODO: we can also use more_itertools.peekable to be more python friendly
                await targetQueryExContext.peek()
                # if there are matching results in the target ex range add it to the priority queue
                await self._orderByPQ.push_async(targetQueryExContext, self._document_producer_comparator)

            except StopAsyncIteration:
                continue

    def _createTargetPartitionQueryExecutionContext(self, partition_key_target_range):

        rewritten_query = self._partitioned_query_ex_info.get_rewritten_query()
        if rewritten_query:
            if isinstance(self._query, dict):
                # this is a parameterized query, collect all the parameters
                query = dict(self._query)
                query["query"] = rewritten_query
            else:
                query = rewritten_query
        else:
            query = self._query

        return document_producer._DocumentProducer(
            partition_key_target_range,
            self._client,
            self._resource_link,
            query,
            self._document_producer_comparator,
            self._options,
        )

    async def _get_target_partition_key_range(self):

        query_ranges = self._partitioned_query_ex_info.get_query_ranges()
        return await self._routing_provider.get_overlapping_ranges(
            self._resource_link, [routing_range.Range.ParseFromDict(range_as_dict) for range_as_dict in query_ranges]
        )

    async def _configure_partition_ranges(self):
        # will be a list of (partition_min, partition_max) tuples
        targetPartitionRanges = await self._get_target_partition_key_range()

        targetPartitionQueryExecutionContextList = []
        for partitionTargetRange in targetPartitionRanges:
            # create and add the child execution context for the target range
            targetPartitionQueryExecutionContextList.append(
                self._createTargetPartitionQueryExecutionContext(partitionTargetRange)
            )

        for targetQueryExContext in targetPartitionQueryExecutionContextList:
            try:
                # TODO: we can also use more_itertools.peekable to be more python friendly
                await targetQueryExContext.peek()
                # if there are matching results in the target ex range add it to the priority queue

                await self._orderByPQ.push_async(targetQueryExContext, self._document_producer_comparator)

            except exceptions.CosmosHttpResponseError as e:
                if exceptions._partition_range_is_gone(e):
                    # repairing document producer context on partition split
                    await self._repair_document_producer()
                else:
                    raise

            except StopAsyncIteration:
                continue
