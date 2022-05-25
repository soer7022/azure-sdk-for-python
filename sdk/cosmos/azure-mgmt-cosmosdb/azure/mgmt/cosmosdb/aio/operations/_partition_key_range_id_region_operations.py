# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, AsyncIterable, Callable, Dict, Optional, TypeVar

from azure.core.async_paging import AsyncItemPaged, AsyncList
from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._partition_key_range_id_region_operations import build_list_metrics_request
T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class PartitionKeyRangeIdRegionOperations:
    """PartitionKeyRangeIdRegionOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.mgmt.cosmosdb.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = _models

    def __init__(self, client, config, serializer, deserializer) -> None:
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    @distributed_trace
    def list_metrics(
        self,
        resource_group_name: str,
        account_name: str,
        region: str,
        database_rid: str,
        collection_rid: str,
        partition_key_range_id: str,
        filter: str,
        **kwargs: Any
    ) -> AsyncIterable["_models.PartitionMetricListResult"]:
        """Retrieves the metrics determined by the given filter for the given partition key range id and
        region.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
        :type resource_group_name: str
        :param account_name: Cosmos DB database account name.
        :type account_name: str
        :param region: Cosmos DB region, with spaces between words and each word capitalized.
        :type region: str
        :param database_rid: Cosmos DB database rid.
        :type database_rid: str
        :param collection_rid: Cosmos DB collection rid.
        :type collection_rid: str
        :param partition_key_range_id: Partition Key Range Id for which to get data.
        :type partition_key_range_id: str
        :param filter: An OData filter expression that describes a subset of metrics to return. The
         parameters that can be filtered are name.value (name of the metric, can have an or of multiple
         names), startTime, endTime, and timeGrain. The supported operator is eq.
        :type filter: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either PartitionMetricListResult or the result of
         cls(response)
        :rtype:
         ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.cosmosdb.models.PartitionMetricListResult]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        api_version = kwargs.pop('api_version', "2022-02-15-preview")  # type: str

        cls = kwargs.pop('cls', None)  # type: ClsType["_models.PartitionMetricListResult"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        def prepare_request(next_link=None):
            if not next_link:
                
                request = build_list_metrics_request(
                    subscription_id=self._config.subscription_id,
                    resource_group_name=resource_group_name,
                    account_name=account_name,
                    region=region,
                    database_rid=database_rid,
                    collection_rid=collection_rid,
                    partition_key_range_id=partition_key_range_id,
                    api_version=api_version,
                    filter=filter,
                    template_url=self.list_metrics.metadata['url'],
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)

            else:
                
                request = build_list_metrics_request(
                    subscription_id=self._config.subscription_id,
                    resource_group_name=resource_group_name,
                    account_name=account_name,
                    region=region,
                    database_rid=database_rid,
                    collection_rid=collection_rid,
                    partition_key_range_id=partition_key_range_id,
                    api_version=api_version,
                    filter=filter,
                    template_url=next_link,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)
                request.method = "GET"
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize("PartitionMetricListResult", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
                request,
                stream=False,
                **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, error_format=ARMErrorFormat)

            return pipeline_response


        return AsyncItemPaged(
            get_next, extract_data
        )
    list_metrics.metadata = {'url': "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/region/{region}/databases/{databaseRid}/collections/{collectionRid}/partitionKeyRangeId/{partitionKeyRangeId}/metrics"}  # type: ignore
