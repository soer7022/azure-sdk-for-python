# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import TYPE_CHECKING

from msrest import Serializer

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpResponse
from azure.core.polling import LROPoller, NoPolling, PollingMethod
from azure.core.polling.base_polling import LROBasePolling
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace

from .. import models as _models
from .._vendor import _convert_request, _format_url_section

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Optional, TypeVar, Union
    T = TypeVar('T')
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False
# fmt: off

def build_full_backup_request_initial(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    api_version = kwargs.pop('api_version', "7.3")  # type: str
    content_type = kwargs.pop('content_type', None)  # type: Optional[str]

    accept = "application/json"
    # Construct URL
    _url = kwargs.pop("template_url", "/backup")

    # Construct parameters
    _query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    _query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    _header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if content_type is not None:
        _header_parameters['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    _header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="POST",
        url=_url,
        params=_query_parameters,
        headers=_header_parameters,
        **kwargs
    )


def build_full_backup_status_request(
    job_id,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    api_version = kwargs.pop('api_version', "7.3")  # type: str

    accept = "application/json"
    # Construct URL
    _url = kwargs.pop("template_url", "/backup/{jobId}/pending")
    path_format_arguments = {
        "jobId": _SERIALIZER.url("job_id", job_id, 'str'),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    _query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    _header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    _header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=_url,
        params=_query_parameters,
        headers=_header_parameters,
        **kwargs
    )


def build_full_restore_operation_request_initial(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    api_version = kwargs.pop('api_version', "7.3")  # type: str
    content_type = kwargs.pop('content_type', None)  # type: Optional[str]

    accept = "application/json"
    # Construct URL
    _url = kwargs.pop("template_url", "/restore")

    # Construct parameters
    _query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    _query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    _header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if content_type is not None:
        _header_parameters['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    _header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="PUT",
        url=_url,
        params=_query_parameters,
        headers=_header_parameters,
        **kwargs
    )


def build_restore_status_request(
    job_id,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    api_version = kwargs.pop('api_version', "7.3")  # type: str

    accept = "application/json"
    # Construct URL
    _url = kwargs.pop("template_url", "/restore/{jobId}/pending")
    path_format_arguments = {
        "jobId": _SERIALIZER.url("job_id", job_id, 'str'),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    _query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    _header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    _header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=_url,
        params=_query_parameters,
        headers=_header_parameters,
        **kwargs
    )


def build_selective_key_restore_operation_request_initial(
    key_name,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    api_version = kwargs.pop('api_version', "7.3")  # type: str
    content_type = kwargs.pop('content_type', None)  # type: Optional[str]

    accept = "application/json"
    # Construct URL
    _url = kwargs.pop("template_url", "/keys/{keyName}/restore")
    path_format_arguments = {
        "keyName": _SERIALIZER.url("key_name", key_name, 'str'),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    _query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    _header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if content_type is not None:
        _header_parameters['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    _header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="PUT",
        url=_url,
        params=_query_parameters,
        headers=_header_parameters,
        **kwargs
    )

# fmt: on
class KeyVaultClientOperationsMixin(object):

    def _full_backup_initial(
        self,
        vault_base_url,  # type: str
        azure_storage_blob_container_uri=None,  # type: Optional["_models.SASTokenParameter"]
        **kwargs  # type: Any
    ):
        # type: (...) -> "_models.FullBackupOperation"
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.FullBackupOperation"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        api_version = kwargs.pop('api_version', "7.3")  # type: str
        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        if azure_storage_blob_container_uri is not None:
            _json = self._serialize.body(azure_storage_blob_container_uri, 'SASTokenParameter')
        else:
            _json = None

        request = build_full_backup_request_initial(
            api_version=api_version,
            content_type=content_type,
            json=_json,
            template_url=self._full_backup_initial.metadata['url'],
        )
        request = _convert_request(request)
        path_format_arguments = {
            "vaultBaseUrl": self._serialize.url("vault_base_url", vault_base_url, 'str', skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)

        pipeline_response = self._client._pipeline.run(  # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        response_headers = {}
        response_headers['Retry-After']=self._deserialize('int', response.headers.get('Retry-After'))
        response_headers['Azure-AsyncOperation']=self._deserialize('str', response.headers.get('Azure-AsyncOperation'))

        deserialized = self._deserialize('FullBackupOperation', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, response_headers)

        return deserialized

    _full_backup_initial.metadata = {'url': "/backup"}  # type: ignore


    @distributed_trace
    def begin_full_backup(
        self,
        vault_base_url,  # type: str
        azure_storage_blob_container_uri=None,  # type: Optional["_models.SASTokenParameter"]
        **kwargs  # type: Any
    ):
        # type: (...) -> LROPoller["_models.FullBackupOperation"]
        """Creates a full backup using a user-provided SAS token to an Azure blob storage container. This
        operation is supported only by the Managed HSM service.

        :param vault_base_url: The vault name, for example https://myvault.vault.azure.net.
        :type vault_base_url: str
        :param azure_storage_blob_container_uri: Azure blob shared access signature token pointing to a
         valid Azure blob container where full backup needs to be stored. This token needs to be valid
         for at least next 24 hours from the time of making this call. Default value is None.
        :type azure_storage_blob_container_uri: ~azure.keyvault.v7_3.models.SASTokenParameter
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be LROBasePolling. Pass in False for
         this operation to not poll, or pass in your own initialized polling object for a personal
         polling strategy.
        :paramtype polling: bool or ~azure.core.polling.PollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of LROPoller that returns either FullBackupOperation or the result of
         cls(response)
        :rtype: ~azure.core.polling.LROPoller[~azure.keyvault.v7_3.models.FullBackupOperation]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        api_version = kwargs.pop('api_version', "7.3")  # type: str
        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]
        polling = kwargs.pop('polling', True)  # type: Union[bool, PollingMethod]
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.FullBackupOperation"]
        lro_delay = kwargs.pop(
            'polling_interval',
            self._config.polling_interval
        )
        cont_token = kwargs.pop('continuation_token', None)  # type: Optional[str]
        if cont_token is None:
            raw_result = self._full_backup_initial(
                vault_base_url=vault_base_url,
                azure_storage_blob_container_uri=azure_storage_blob_container_uri,
                api_version=api_version,
                content_type=content_type,
                cls=lambda x,y,z: x,
                **kwargs
            )
        kwargs.pop('error_map', None)

        def get_long_running_output(pipeline_response):
            response_headers = {}
            response = pipeline_response.http_response
            response_headers['Retry-After']=self._deserialize('int', response.headers.get('Retry-After'))
            response_headers['Azure-AsyncOperation']=self._deserialize('str', response.headers.get('Azure-AsyncOperation'))
            
            deserialized = self._deserialize('FullBackupOperation', pipeline_response)
            if cls:
                return cls(pipeline_response, deserialized, response_headers)
            return deserialized


        path_format_arguments = {
            "vaultBaseUrl": self._serialize.url("vault_base_url", vault_base_url, 'str', skip_quote=True),
        }

        if polling is True: polling_method = LROBasePolling(lro_delay, lro_options={'final-state-via': 'azure-async-operation'}, path_format_arguments=path_format_arguments, **kwargs)
        elif polling is False: polling_method = NoPolling()
        else: polling_method = polling
        if cont_token:
            return LROPoller.from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output
            )
        return LROPoller(self._client, raw_result, get_long_running_output, polling_method)

    begin_full_backup.metadata = {'url': "/backup"}  # type: ignore

    @distributed_trace
    def full_backup_status(
        self,
        vault_base_url,  # type: str
        job_id,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> "_models.FullBackupOperation"
        """Returns the status of full backup operation.

        :param vault_base_url: The vault name, for example https://myvault.vault.azure.net.
        :type vault_base_url: str
        :param job_id: The id returned as part of the backup request.
        :type job_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: FullBackupOperation, or the result of cls(response)
        :rtype: ~azure.keyvault.v7_3.models.FullBackupOperation
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.FullBackupOperation"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        api_version = kwargs.pop('api_version', "7.3")  # type: str

        
        request = build_full_backup_status_request(
            job_id=job_id,
            api_version=api_version,
            template_url=self.full_backup_status.metadata['url'],
        )
        request = _convert_request(request)
        path_format_arguments = {
            "vaultBaseUrl": self._serialize.url("vault_base_url", vault_base_url, 'str', skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)

        pipeline_response = self._client._pipeline.run(  # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.KeyVaultError, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('FullBackupOperation', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    full_backup_status.metadata = {'url': "/backup/{jobId}/pending"}  # type: ignore


    def _full_restore_operation_initial(
        self,
        vault_base_url,  # type: str
        restore_blob_details=None,  # type: Optional["_models.RestoreOperationParameters"]
        **kwargs  # type: Any
    ):
        # type: (...) -> "_models.RestoreOperation"
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.RestoreOperation"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        api_version = kwargs.pop('api_version', "7.3")  # type: str
        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        if restore_blob_details is not None:
            _json = self._serialize.body(restore_blob_details, 'RestoreOperationParameters')
        else:
            _json = None

        request = build_full_restore_operation_request_initial(
            api_version=api_version,
            content_type=content_type,
            json=_json,
            template_url=self._full_restore_operation_initial.metadata['url'],
        )
        request = _convert_request(request)
        path_format_arguments = {
            "vaultBaseUrl": self._serialize.url("vault_base_url", vault_base_url, 'str', skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)

        pipeline_response = self._client._pipeline.run(  # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        response_headers = {}
        response_headers['Retry-After']=self._deserialize('int', response.headers.get('Retry-After'))
        response_headers['Azure-AsyncOperation']=self._deserialize('str', response.headers.get('Azure-AsyncOperation'))

        deserialized = self._deserialize('RestoreOperation', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, response_headers)

        return deserialized

    _full_restore_operation_initial.metadata = {'url': "/restore"}  # type: ignore


    @distributed_trace
    def begin_full_restore_operation(
        self,
        vault_base_url,  # type: str
        restore_blob_details=None,  # type: Optional["_models.RestoreOperationParameters"]
        **kwargs  # type: Any
    ):
        # type: (...) -> LROPoller["_models.RestoreOperation"]
        """Restores all key materials using the SAS token pointing to a previously stored Azure Blob
        storage backup folder.

        :param vault_base_url: The vault name, for example https://myvault.vault.azure.net.
        :type vault_base_url: str
        :param restore_blob_details: The Azure blob SAS token pointing to a folder where the previous
         successful full backup was stored. Default value is None.
        :type restore_blob_details: ~azure.keyvault.v7_3.models.RestoreOperationParameters
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be LROBasePolling. Pass in False for
         this operation to not poll, or pass in your own initialized polling object for a personal
         polling strategy.
        :paramtype polling: bool or ~azure.core.polling.PollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of LROPoller that returns either RestoreOperation or the result of
         cls(response)
        :rtype: ~azure.core.polling.LROPoller[~azure.keyvault.v7_3.models.RestoreOperation]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        api_version = kwargs.pop('api_version', "7.3")  # type: str
        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]
        polling = kwargs.pop('polling', True)  # type: Union[bool, PollingMethod]
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.RestoreOperation"]
        lro_delay = kwargs.pop(
            'polling_interval',
            self._config.polling_interval
        )
        cont_token = kwargs.pop('continuation_token', None)  # type: Optional[str]
        if cont_token is None:
            raw_result = self._full_restore_operation_initial(
                vault_base_url=vault_base_url,
                restore_blob_details=restore_blob_details,
                api_version=api_version,
                content_type=content_type,
                cls=lambda x,y,z: x,
                **kwargs
            )
        kwargs.pop('error_map', None)

        def get_long_running_output(pipeline_response):
            response_headers = {}
            response = pipeline_response.http_response
            response_headers['Retry-After']=self._deserialize('int', response.headers.get('Retry-After'))
            response_headers['Azure-AsyncOperation']=self._deserialize('str', response.headers.get('Azure-AsyncOperation'))
            
            deserialized = self._deserialize('RestoreOperation', pipeline_response)
            if cls:
                return cls(pipeline_response, deserialized, response_headers)
            return deserialized


        path_format_arguments = {
            "vaultBaseUrl": self._serialize.url("vault_base_url", vault_base_url, 'str', skip_quote=True),
        }

        if polling is True: polling_method = LROBasePolling(lro_delay, lro_options={'final-state-via': 'azure-async-operation'}, path_format_arguments=path_format_arguments, **kwargs)
        elif polling is False: polling_method = NoPolling()
        else: polling_method = polling
        if cont_token:
            return LROPoller.from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output
            )
        return LROPoller(self._client, raw_result, get_long_running_output, polling_method)

    begin_full_restore_operation.metadata = {'url': "/restore"}  # type: ignore

    @distributed_trace
    def restore_status(
        self,
        vault_base_url,  # type: str
        job_id,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> "_models.RestoreOperation"
        """Returns the status of restore operation.

        :param vault_base_url: The vault name, for example https://myvault.vault.azure.net.
        :type vault_base_url: str
        :param job_id: The Job Id returned part of the restore operation.
        :type job_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: RestoreOperation, or the result of cls(response)
        :rtype: ~azure.keyvault.v7_3.models.RestoreOperation
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.RestoreOperation"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        api_version = kwargs.pop('api_version', "7.3")  # type: str

        
        request = build_restore_status_request(
            job_id=job_id,
            api_version=api_version,
            template_url=self.restore_status.metadata['url'],
        )
        request = _convert_request(request)
        path_format_arguments = {
            "vaultBaseUrl": self._serialize.url("vault_base_url", vault_base_url, 'str', skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)

        pipeline_response = self._client._pipeline.run(  # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.KeyVaultError, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('RestoreOperation', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    restore_status.metadata = {'url': "/restore/{jobId}/pending"}  # type: ignore


    def _selective_key_restore_operation_initial(
        self,
        vault_base_url,  # type: str
        key_name,  # type: str
        restore_blob_details=None,  # type: Optional["_models.SelectiveKeyRestoreOperationParameters"]
        **kwargs  # type: Any
    ):
        # type: (...) -> "_models.SelectiveKeyRestoreOperation"
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.SelectiveKeyRestoreOperation"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        api_version = kwargs.pop('api_version', "7.3")  # type: str
        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        if restore_blob_details is not None:
            _json = self._serialize.body(restore_blob_details, 'SelectiveKeyRestoreOperationParameters')
        else:
            _json = None

        request = build_selective_key_restore_operation_request_initial(
            key_name=key_name,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            template_url=self._selective_key_restore_operation_initial.metadata['url'],
        )
        request = _convert_request(request)
        path_format_arguments = {
            "vaultBaseUrl": self._serialize.url("vault_base_url", vault_base_url, 'str', skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)

        pipeline_response = self._client._pipeline.run(  # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        response_headers = {}
        response_headers['Retry-After']=self._deserialize('int', response.headers.get('Retry-After'))
        response_headers['Azure-AsyncOperation']=self._deserialize('str', response.headers.get('Azure-AsyncOperation'))

        deserialized = self._deserialize('SelectiveKeyRestoreOperation', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, response_headers)

        return deserialized

    _selective_key_restore_operation_initial.metadata = {'url': "/keys/{keyName}/restore"}  # type: ignore


    @distributed_trace
    def begin_selective_key_restore_operation(
        self,
        vault_base_url,  # type: str
        key_name,  # type: str
        restore_blob_details=None,  # type: Optional["_models.SelectiveKeyRestoreOperationParameters"]
        **kwargs  # type: Any
    ):
        # type: (...) -> LROPoller["_models.SelectiveKeyRestoreOperation"]
        """Restores all key versions of a given key using user supplied SAS token pointing to a previously
        stored Azure Blob storage backup folder.

        :param vault_base_url: The vault name, for example https://myvault.vault.azure.net.
        :type vault_base_url: str
        :param key_name: The name of the key to be restored from the user supplied backup.
        :type key_name: str
        :param restore_blob_details: The Azure blob SAS token pointing to a folder where the previous
         successful full backup was stored. Default value is None.
        :type restore_blob_details: ~azure.keyvault.v7_3.models.SelectiveKeyRestoreOperationParameters
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be LROBasePolling. Pass in False for
         this operation to not poll, or pass in your own initialized polling object for a personal
         polling strategy.
        :paramtype polling: bool or ~azure.core.polling.PollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of LROPoller that returns either SelectiveKeyRestoreOperation or the
         result of cls(response)
        :rtype: ~azure.core.polling.LROPoller[~azure.keyvault.v7_3.models.SelectiveKeyRestoreOperation]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        api_version = kwargs.pop('api_version', "7.3")  # type: str
        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]
        polling = kwargs.pop('polling', True)  # type: Union[bool, PollingMethod]
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.SelectiveKeyRestoreOperation"]
        lro_delay = kwargs.pop(
            'polling_interval',
            self._config.polling_interval
        )
        cont_token = kwargs.pop('continuation_token', None)  # type: Optional[str]
        if cont_token is None:
            raw_result = self._selective_key_restore_operation_initial(
                vault_base_url=vault_base_url,
                key_name=key_name,
                restore_blob_details=restore_blob_details,
                api_version=api_version,
                content_type=content_type,
                cls=lambda x,y,z: x,
                **kwargs
            )
        kwargs.pop('error_map', None)

        def get_long_running_output(pipeline_response):
            response_headers = {}
            response = pipeline_response.http_response
            response_headers['Retry-After']=self._deserialize('int', response.headers.get('Retry-After'))
            response_headers['Azure-AsyncOperation']=self._deserialize('str', response.headers.get('Azure-AsyncOperation'))
            
            deserialized = self._deserialize('SelectiveKeyRestoreOperation', pipeline_response)
            if cls:
                return cls(pipeline_response, deserialized, response_headers)
            return deserialized


        path_format_arguments = {
            "vaultBaseUrl": self._serialize.url("vault_base_url", vault_base_url, 'str', skip_quote=True),
        }

        if polling is True: polling_method = LROBasePolling(lro_delay, lro_options={'final-state-via': 'azure-async-operation'}, path_format_arguments=path_format_arguments, **kwargs)
        elif polling is False: polling_method = NoPolling()
        else: polling_method = polling
        if cont_token:
            return LROPoller.from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output
            )
        return LROPoller(self._client, raw_result, get_long_running_output, polling_method)

    begin_selective_key_restore_operation.metadata = {'url': "/keys/{keyName}/restore"}  # type: ignore
