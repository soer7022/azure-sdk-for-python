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
from azure.core.pipeline.transport import HttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.mgmt.core.exceptions import ARMErrorFormat
from msrest import Serializer

from .. import models as _models
from .._vendor import _convert_request, _format_url_section
T = TypeVar('T')
JSONType = Any
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False

def build_list_logs_request(
    subscription_id: str,
    resource_group_name: str,
    container_group_name: str,
    container_name: str,
    *,
    tail: Optional[int] = None,
    timestamps: Optional[bool] = None,
    **kwargs: Any
) -> HttpRequest:
    api_version = "2021-10-01"
    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerInstance/containerGroups/{containerGroupName}/containers/{containerName}/logs')
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, 'str'),
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, 'str'),
        "containerGroupName": _SERIALIZER.url("container_group_name", container_group_name, 'str'),
        "containerName": _SERIALIZER.url("container_name", container_name, 'str'),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')
    if tail is not None:
        query_parameters['tail'] = _SERIALIZER.query("tail", tail, 'int')
    if timestamps is not None:
        query_parameters['timestamps'] = _SERIALIZER.query("timestamps", timestamps, 'bool')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        **kwargs
    )


def build_execute_command_request(
    subscription_id: str,
    resource_group_name: str,
    container_group_name: str,
    container_name: str,
    *,
    json: JSONType = None,
    content: Any = None,
    **kwargs: Any
) -> HttpRequest:
    content_type = kwargs.pop('content_type', None)  # type: Optional[str]

    api_version = "2021-10-01"
    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerInstance/containerGroups/{containerGroupName}/containers/{containerName}/exec')
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, 'str'),
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, 'str'),
        "containerGroupName": _SERIALIZER.url("container_group_name", container_group_name, 'str'),
        "containerName": _SERIALIZER.url("container_name", container_name, 'str'),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if content_type is not None:
        header_parameters['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="POST",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        json=json,
        content=content,
        **kwargs
    )


def build_attach_request(
    subscription_id: str,
    resource_group_name: str,
    container_group_name: str,
    container_name: str,
    **kwargs: Any
) -> HttpRequest:
    api_version = "2021-10-01"
    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerInstance/containerGroups/{containerGroupName}/containers/{containerName}/attach')
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, 'str'),
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, 'str'),
        "containerGroupName": _SERIALIZER.url("container_group_name", container_group_name, 'str'),
        "containerName": _SERIALIZER.url("container_name", container_name, 'str'),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="POST",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        **kwargs
    )

class ContainersOperations(object):
    """ContainersOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.mgmt.containerinstance.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = _models

    def __init__(self, client, config, serializer, deserializer):
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    @distributed_trace
    def list_logs(
        self,
        resource_group_name: str,
        container_group_name: str,
        container_name: str,
        tail: Optional[int] = None,
        timestamps: Optional[bool] = None,
        **kwargs: Any
    ) -> "_models.Logs":
        """Get the logs for a specified container instance.

        Get the logs for a specified container instance in a specified resource group and container
        group.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param container_group_name: The name of the container group.
        :type container_group_name: str
        :param container_name: The name of the container instance.
        :type container_name: str
        :param tail: The number of lines to show from the tail of the container instance log. If not
         provided, all available logs are shown up to 4mb.
        :type tail: int
        :param timestamps: If true, adds a timestamp at the beginning of every line of log output. If
         not provided, defaults to false.
        :type timestamps: bool
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Logs, or the result of cls(response)
        :rtype: ~azure.mgmt.containerinstance.models.Logs
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.Logs"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        
        request = build_list_logs_request(
            subscription_id=self._config.subscription_id,
            resource_group_name=resource_group_name,
            container_group_name=container_group_name,
            container_name=container_name,
            tail=tail,
            timestamps=timestamps,
            template_url=self.list_logs.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('Logs', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    list_logs.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerInstance/containerGroups/{containerGroupName}/containers/{containerName}/logs'}  # type: ignore


    @distributed_trace
    def execute_command(
        self,
        resource_group_name: str,
        container_group_name: str,
        container_name: str,
        container_exec_request: "_models.ContainerExecRequest",
        **kwargs: Any
    ) -> "_models.ContainerExecResponse":
        """Executes a command in a specific container instance.

        Executes a command for a specific container instance in a specified resource group and
        container group.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param container_group_name: The name of the container group.
        :type container_group_name: str
        :param container_name: The name of the container instance.
        :type container_name: str
        :param container_exec_request: The request for the exec command.
        :type container_exec_request: ~azure.mgmt.containerinstance.models.ContainerExecRequest
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ContainerExecResponse, or the result of cls(response)
        :rtype: ~azure.mgmt.containerinstance.models.ContainerExecResponse
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.ContainerExecResponse"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        _json = self._serialize.body(container_exec_request, 'ContainerExecRequest')

        request = build_execute_command_request(
            subscription_id=self._config.subscription_id,
            resource_group_name=resource_group_name,
            container_group_name=container_group_name,
            container_name=container_name,
            content_type=content_type,
            json=_json,
            template_url=self.execute_command.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('ContainerExecResponse', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    execute_command.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerInstance/containerGroups/{containerGroupName}/containers/{containerName}/exec'}  # type: ignore


    @distributed_trace
    def attach(
        self,
        resource_group_name: str,
        container_group_name: str,
        container_name: str,
        **kwargs: Any
    ) -> "_models.ContainerAttachResponse":
        """Attach to the output of a specific container instance.

        Attach to the output stream of a specific container instance in a specified resource group and
        container group.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param container_group_name: The name of the container group.
        :type container_group_name: str
        :param container_name: The name of the container instance.
        :type container_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ContainerAttachResponse, or the result of cls(response)
        :rtype: ~azure.mgmt.containerinstance.models.ContainerAttachResponse
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.ContainerAttachResponse"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        
        request = build_attach_request(
            subscription_id=self._config.subscription_id,
            resource_group_name=resource_group_name,
            container_group_name=container_group_name,
            container_name=container_name,
            template_url=self.attach.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('ContainerAttachResponse', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    attach.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerInstance/containerGroups/{containerGroupName}/containers/{containerName}/attach'}  # type: ignore

