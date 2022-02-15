# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import functools
from typing import Any, Callable, Dict, Generic, Optional, TypeVar
import warnings

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._queue_services_operations import build_get_service_properties_request, build_list_request, build_set_service_properties_request
T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class QueueServicesOperations:
    """QueueServicesOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.mgmt.storage.v2021_08_01.models
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

    @distributed_trace_async
    async def list(
        self,
        resource_group_name: str,
        account_name: str,
        **kwargs: Any
    ) -> "_models.ListQueueServices":
        """List all queue services for the storage account.

        :param resource_group_name: The name of the resource group within the user's subscription. The
         name is case insensitive.
        :type resource_group_name: str
        :param account_name: The name of the storage account within the specified resource group.
         Storage account names must be between 3 and 24 characters in length and use numbers and
         lower-case letters only.
        :type account_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ListQueueServices, or the result of cls(response)
        :rtype: ~azure.mgmt.storage.v2021_08_01.models.ListQueueServices
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.ListQueueServices"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        
        request = build_list_request(
            resource_group_name=resource_group_name,
            account_name=account_name,
            subscription_id=self._config.subscription_id,
            template_url=self.list.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('ListQueueServices', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    list.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}/queueServices'}  # type: ignore


    @distributed_trace_async
    async def set_service_properties(
        self,
        resource_group_name: str,
        account_name: str,
        parameters: "_models.QueueServiceProperties",
        **kwargs: Any
    ) -> "_models.QueueServiceProperties":
        """Sets the properties of a storage account’s Queue service, including properties for Storage
        Analytics and CORS (Cross-Origin Resource Sharing) rules.

        :param resource_group_name: The name of the resource group within the user's subscription. The
         name is case insensitive.
        :type resource_group_name: str
        :param account_name: The name of the storage account within the specified resource group.
         Storage account names must be between 3 and 24 characters in length and use numbers and
         lower-case letters only.
        :type account_name: str
        :param parameters: The properties of a storage account’s Queue service, only properties for
         Storage Analytics and CORS (Cross-Origin Resource Sharing) rules can be specified.
        :type parameters: ~azure.mgmt.storage.v2021_08_01.models.QueueServiceProperties
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: QueueServiceProperties, or the result of cls(response)
        :rtype: ~azure.mgmt.storage.v2021_08_01.models.QueueServiceProperties
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.QueueServiceProperties"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        _json = self._serialize.body(parameters, 'QueueServiceProperties')

        request = build_set_service_properties_request(
            resource_group_name=resource_group_name,
            account_name=account_name,
            subscription_id=self._config.subscription_id,
            content_type=content_type,
            json=_json,
            template_url=self.set_service_properties.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('QueueServiceProperties', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    set_service_properties.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}/queueServices/{queueServiceName}'}  # type: ignore


    @distributed_trace_async
    async def get_service_properties(
        self,
        resource_group_name: str,
        account_name: str,
        **kwargs: Any
    ) -> "_models.QueueServiceProperties":
        """Gets the properties of a storage account’s Queue service, including properties for Storage
        Analytics and CORS (Cross-Origin Resource Sharing) rules.

        :param resource_group_name: The name of the resource group within the user's subscription. The
         name is case insensitive.
        :type resource_group_name: str
        :param account_name: The name of the storage account within the specified resource group.
         Storage account names must be between 3 and 24 characters in length and use numbers and
         lower-case letters only.
        :type account_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: QueueServiceProperties, or the result of cls(response)
        :rtype: ~azure.mgmt.storage.v2021_08_01.models.QueueServiceProperties
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.QueueServiceProperties"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        
        request = build_get_service_properties_request(
            resource_group_name=resource_group_name,
            account_name=account_name,
            subscription_id=self._config.subscription_id,
            template_url=self.get_service_properties.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('QueueServiceProperties', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_service_properties.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}/queueServices/{queueServiceName}'}  # type: ignore

