# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, AsyncIterable, Callable, Dict, Generic, Optional, TypeVar
import warnings

from azure.core.async_paging import AsyncItemPaged, AsyncList
from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models as _models

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class ConfigurationAssignmentsOperations:
    """ConfigurationAssignmentsOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.mgmt.maintenance.models
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

    async def get_parent(
        self,
        resource_group_name: str,
        provider_name: str,
        resource_parent_type: str,
        resource_parent_name: str,
        resource_type: str,
        resource_name: str,
        configuration_assignment_name: str,
        **kwargs: Any
    ) -> "_models.ConfigurationAssignment":
        """Get configuration assignment.

        Get configuration for resource.

        :param resource_group_name: Resource group name.
        :type resource_group_name: str
        :param provider_name: Resource provider name.
        :type provider_name: str
        :param resource_parent_type: Resource parent type.
        :type resource_parent_type: str
        :param resource_parent_name: Resource parent identifier.
        :type resource_parent_name: str
        :param resource_type: Resource type.
        :type resource_type: str
        :param resource_name: Resource identifier.
        :type resource_name: str
        :param configuration_assignment_name: Configuration assignment name.
        :type configuration_assignment_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ConfigurationAssignment, or the result of cls(response)
        :rtype: ~azure.mgmt.maintenance.models.ConfigurationAssignment
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.ConfigurationAssignment"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2021-09-01-preview"
        accept = "application/json"

        # Construct URL
        url = self.get_parent.metadata['url']  # type: ignore
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'providerName': self._serialize.url("provider_name", provider_name, 'str'),
            'resourceParentType': self._serialize.url("resource_parent_type", resource_parent_type, 'str'),
            'resourceParentName': self._serialize.url("resource_parent_name", resource_parent_name, 'str'),
            'resourceType': self._serialize.url("resource_type", resource_type, 'str'),
            'resourceName': self._serialize.url("resource_name", resource_name, 'str'),
            'configurationAssignmentName': self._serialize.url("configuration_assignment_name", configuration_assignment_name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.MaintenanceError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('ConfigurationAssignment', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_parent.metadata = {'url': '/subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/{providerName}/{resourceParentType}/{resourceParentName}/{resourceType}/{resourceName}/providers/Microsoft.Maintenance/configurationAssignments/{configurationAssignmentName}'}  # type: ignore

    async def create_or_update_parent(
        self,
        resource_group_name: str,
        provider_name: str,
        resource_parent_type: str,
        resource_parent_name: str,
        resource_type: str,
        resource_name: str,
        configuration_assignment_name: str,
        configuration_assignment: "_models.ConfigurationAssignment",
        **kwargs: Any
    ) -> "_models.ConfigurationAssignment":
        """Create configuration assignment.

        Register configuration for resource.

        :param resource_group_name: Resource group name.
        :type resource_group_name: str
        :param provider_name: Resource provider name.
        :type provider_name: str
        :param resource_parent_type: Resource parent type.
        :type resource_parent_type: str
        :param resource_parent_name: Resource parent identifier.
        :type resource_parent_name: str
        :param resource_type: Resource type.
        :type resource_type: str
        :param resource_name: Resource identifier.
        :type resource_name: str
        :param configuration_assignment_name: Configuration assignment name.
        :type configuration_assignment_name: str
        :param configuration_assignment: The configurationAssignment.
        :type configuration_assignment: ~azure.mgmt.maintenance.models.ConfigurationAssignment
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ConfigurationAssignment, or the result of cls(response)
        :rtype: ~azure.mgmt.maintenance.models.ConfigurationAssignment
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.ConfigurationAssignment"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2021-09-01-preview"
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.create_or_update_parent.metadata['url']  # type: ignore
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'providerName': self._serialize.url("provider_name", provider_name, 'str'),
            'resourceParentType': self._serialize.url("resource_parent_type", resource_parent_type, 'str'),
            'resourceParentName': self._serialize.url("resource_parent_name", resource_parent_name, 'str'),
            'resourceType': self._serialize.url("resource_type", resource_type, 'str'),
            'resourceName': self._serialize.url("resource_name", resource_name, 'str'),
            'configurationAssignmentName': self._serialize.url("configuration_assignment_name", configuration_assignment_name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(configuration_assignment, 'ConfigurationAssignment')
        body_content_kwargs['content'] = body_content
        request = self._client.put(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.MaintenanceError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('ConfigurationAssignment', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    create_or_update_parent.metadata = {'url': '/subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/{providerName}/{resourceParentType}/{resourceParentName}/{resourceType}/{resourceName}/providers/Microsoft.Maintenance/configurationAssignments/{configurationAssignmentName}'}  # type: ignore

    async def delete_parent(
        self,
        resource_group_name: str,
        provider_name: str,
        resource_parent_type: str,
        resource_parent_name: str,
        resource_type: str,
        resource_name: str,
        configuration_assignment_name: str,
        **kwargs: Any
    ) -> Optional["_models.ConfigurationAssignment"]:
        """Unregister configuration for resource.

        Unregister configuration for resource.

        :param resource_group_name: Resource group name.
        :type resource_group_name: str
        :param provider_name: Resource provider name.
        :type provider_name: str
        :param resource_parent_type: Resource parent type.
        :type resource_parent_type: str
        :param resource_parent_name: Resource parent identifier.
        :type resource_parent_name: str
        :param resource_type: Resource type.
        :type resource_type: str
        :param resource_name: Resource identifier.
        :type resource_name: str
        :param configuration_assignment_name: Unique configuration assignment name.
        :type configuration_assignment_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ConfigurationAssignment, or the result of cls(response)
        :rtype: ~azure.mgmt.maintenance.models.ConfigurationAssignment or None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[Optional["_models.ConfigurationAssignment"]]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2021-09-01-preview"
        accept = "application/json"

        # Construct URL
        url = self.delete_parent.metadata['url']  # type: ignore
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'providerName': self._serialize.url("provider_name", provider_name, 'str'),
            'resourceParentType': self._serialize.url("resource_parent_type", resource_parent_type, 'str'),
            'resourceParentName': self._serialize.url("resource_parent_name", resource_parent_name, 'str'),
            'resourceType': self._serialize.url("resource_type", resource_type, 'str'),
            'resourceName': self._serialize.url("resource_name", resource_name, 'str'),
            'configurationAssignmentName': self._serialize.url("configuration_assignment_name", configuration_assignment_name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.delete(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.MaintenanceError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('ConfigurationAssignment', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    delete_parent.metadata = {'url': '/subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/{providerName}/{resourceParentType}/{resourceParentName}/{resourceType}/{resourceName}/providers/Microsoft.Maintenance/configurationAssignments/{configurationAssignmentName}'}  # type: ignore

    async def get(
        self,
        resource_group_name: str,
        provider_name: str,
        resource_type: str,
        resource_name: str,
        configuration_assignment_name: str,
        **kwargs: Any
    ) -> "_models.ConfigurationAssignment":
        """Get configuration assignment.

        Get configuration for resource.

        :param resource_group_name: Resource group name.
        :type resource_group_name: str
        :param provider_name: Resource provider name.
        :type provider_name: str
        :param resource_type: Resource type.
        :type resource_type: str
        :param resource_name: Resource identifier.
        :type resource_name: str
        :param configuration_assignment_name: Configuration assignment name.
        :type configuration_assignment_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ConfigurationAssignment, or the result of cls(response)
        :rtype: ~azure.mgmt.maintenance.models.ConfigurationAssignment
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.ConfigurationAssignment"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2021-09-01-preview"
        accept = "application/json"

        # Construct URL
        url = self.get.metadata['url']  # type: ignore
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'providerName': self._serialize.url("provider_name", provider_name, 'str'),
            'resourceType': self._serialize.url("resource_type", resource_type, 'str'),
            'resourceName': self._serialize.url("resource_name", resource_name, 'str'),
            'configurationAssignmentName': self._serialize.url("configuration_assignment_name", configuration_assignment_name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.MaintenanceError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('ConfigurationAssignment', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get.metadata = {'url': '/subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/{providerName}/{resourceType}/{resourceName}/providers/Microsoft.Maintenance/configurationAssignments/{configurationAssignmentName}'}  # type: ignore

    async def create_or_update(
        self,
        resource_group_name: str,
        provider_name: str,
        resource_type: str,
        resource_name: str,
        configuration_assignment_name: str,
        configuration_assignment: "_models.ConfigurationAssignment",
        **kwargs: Any
    ) -> "_models.ConfigurationAssignment":
        """Create configuration assignment.

        Register configuration for resource.

        :param resource_group_name: Resource group name.
        :type resource_group_name: str
        :param provider_name: Resource provider name.
        :type provider_name: str
        :param resource_type: Resource type.
        :type resource_type: str
        :param resource_name: Resource identifier.
        :type resource_name: str
        :param configuration_assignment_name: Configuration assignment name.
        :type configuration_assignment_name: str
        :param configuration_assignment: The configurationAssignment.
        :type configuration_assignment: ~azure.mgmt.maintenance.models.ConfigurationAssignment
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ConfigurationAssignment, or the result of cls(response)
        :rtype: ~azure.mgmt.maintenance.models.ConfigurationAssignment
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.ConfigurationAssignment"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2021-09-01-preview"
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.create_or_update.metadata['url']  # type: ignore
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'providerName': self._serialize.url("provider_name", provider_name, 'str'),
            'resourceType': self._serialize.url("resource_type", resource_type, 'str'),
            'resourceName': self._serialize.url("resource_name", resource_name, 'str'),
            'configurationAssignmentName': self._serialize.url("configuration_assignment_name", configuration_assignment_name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(configuration_assignment, 'ConfigurationAssignment')
        body_content_kwargs['content'] = body_content
        request = self._client.put(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.MaintenanceError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('ConfigurationAssignment', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    create_or_update.metadata = {'url': '/subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/{providerName}/{resourceType}/{resourceName}/providers/Microsoft.Maintenance/configurationAssignments/{configurationAssignmentName}'}  # type: ignore

    async def delete(
        self,
        resource_group_name: str,
        provider_name: str,
        resource_type: str,
        resource_name: str,
        configuration_assignment_name: str,
        **kwargs: Any
    ) -> Optional["_models.ConfigurationAssignment"]:
        """Unregister configuration for resource.

        Unregister configuration for resource.

        :param resource_group_name: Resource group name.
        :type resource_group_name: str
        :param provider_name: Resource provider name.
        :type provider_name: str
        :param resource_type: Resource type.
        :type resource_type: str
        :param resource_name: Resource identifier.
        :type resource_name: str
        :param configuration_assignment_name: Unique configuration assignment name.
        :type configuration_assignment_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ConfigurationAssignment, or the result of cls(response)
        :rtype: ~azure.mgmt.maintenance.models.ConfigurationAssignment or None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[Optional["_models.ConfigurationAssignment"]]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2021-09-01-preview"
        accept = "application/json"

        # Construct URL
        url = self.delete.metadata['url']  # type: ignore
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'providerName': self._serialize.url("provider_name", provider_name, 'str'),
            'resourceType': self._serialize.url("resource_type", resource_type, 'str'),
            'resourceName': self._serialize.url("resource_name", resource_name, 'str'),
            'configurationAssignmentName': self._serialize.url("configuration_assignment_name", configuration_assignment_name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.delete(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.MaintenanceError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('ConfigurationAssignment', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    delete.metadata = {'url': '/subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/{providerName}/{resourceType}/{resourceName}/providers/Microsoft.Maintenance/configurationAssignments/{configurationAssignmentName}'}  # type: ignore

    def list_parent(
        self,
        resource_group_name: str,
        provider_name: str,
        resource_parent_type: str,
        resource_parent_name: str,
        resource_type: str,
        resource_name: str,
        **kwargs: Any
    ) -> AsyncIterable["_models.ListConfigurationAssignmentsResult"]:
        """List configurationAssignments for resource.

        List configurationAssignments for resource.

        :param resource_group_name: Resource group name.
        :type resource_group_name: str
        :param provider_name: Resource provider name.
        :type provider_name: str
        :param resource_parent_type: Resource parent type.
        :type resource_parent_type: str
        :param resource_parent_name: Resource parent identifier.
        :type resource_parent_name: str
        :param resource_type: Resource type.
        :type resource_type: str
        :param resource_name: Resource identifier.
        :type resource_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either ListConfigurationAssignmentsResult or the result of cls(response)
        :rtype: ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.maintenance.models.ListConfigurationAssignmentsResult]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.ListConfigurationAssignmentsResult"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2021-09-01-preview"
        accept = "application/json"

        def prepare_request(next_link=None):
            # Construct headers
            header_parameters = {}  # type: Dict[str, Any]
            header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

            if not next_link:
                # Construct URL
                url = self.list_parent.metadata['url']  # type: ignore
                path_format_arguments = {
                    'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
                    'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
                    'providerName': self._serialize.url("provider_name", provider_name, 'str'),
                    'resourceParentType': self._serialize.url("resource_parent_type", resource_parent_type, 'str'),
                    'resourceParentName': self._serialize.url("resource_parent_name", resource_parent_name, 'str'),
                    'resourceType': self._serialize.url("resource_type", resource_type, 'str'),
                    'resourceName': self._serialize.url("resource_name", resource_name, 'str'),
                }
                url = self._client.format_url(url, **path_format_arguments)
                # Construct parameters
                query_parameters = {}  # type: Dict[str, Any]
                query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

                request = self._client.get(url, query_parameters, header_parameters)
            else:
                url = next_link
                query_parameters = {}  # type: Dict[str, Any]
                request = self._client.get(url, query_parameters, header_parameters)
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize('ListConfigurationAssignmentsResult', pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                error = self._deserialize.failsafe_deserialize(_models.MaintenanceError, response)
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response

        return AsyncItemPaged(
            get_next, extract_data
        )
    list_parent.metadata = {'url': '/subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/{providerName}/{resourceParentType}/{resourceParentName}/{resourceType}/{resourceName}/providers/Microsoft.Maintenance/configurationAssignments'}  # type: ignore

    def list(
        self,
        resource_group_name: str,
        provider_name: str,
        resource_type: str,
        resource_name: str,
        **kwargs: Any
    ) -> AsyncIterable["_models.ListConfigurationAssignmentsResult"]:
        """List configurationAssignments for resource.

        List configurationAssignments for resource.

        :param resource_group_name: Resource group name.
        :type resource_group_name: str
        :param provider_name: Resource provider name.
        :type provider_name: str
        :param resource_type: Resource type.
        :type resource_type: str
        :param resource_name: Resource identifier.
        :type resource_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either ListConfigurationAssignmentsResult or the result of cls(response)
        :rtype: ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.maintenance.models.ListConfigurationAssignmentsResult]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.ListConfigurationAssignmentsResult"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2021-09-01-preview"
        accept = "application/json"

        def prepare_request(next_link=None):
            # Construct headers
            header_parameters = {}  # type: Dict[str, Any]
            header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

            if not next_link:
                # Construct URL
                url = self.list.metadata['url']  # type: ignore
                path_format_arguments = {
                    'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
                    'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
                    'providerName': self._serialize.url("provider_name", provider_name, 'str'),
                    'resourceType': self._serialize.url("resource_type", resource_type, 'str'),
                    'resourceName': self._serialize.url("resource_name", resource_name, 'str'),
                }
                url = self._client.format_url(url, **path_format_arguments)
                # Construct parameters
                query_parameters = {}  # type: Dict[str, Any]
                query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

                request = self._client.get(url, query_parameters, header_parameters)
            else:
                url = next_link
                query_parameters = {}  # type: Dict[str, Any]
                request = self._client.get(url, query_parameters, header_parameters)
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize('ListConfigurationAssignmentsResult', pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                error = self._deserialize.failsafe_deserialize(_models.MaintenanceError, response)
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response

        return AsyncItemPaged(
            get_next, extract_data
        )
    list.metadata = {'url': '/subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/{providerName}/{resourceType}/{resourceName}/providers/Microsoft.Maintenance/configurationAssignments'}  # type: ignore
