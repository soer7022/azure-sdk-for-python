# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from copy import deepcopy
from typing import Any, Optional, TYPE_CHECKING

from azure.core.rest import HttpRequest, HttpResponse
from azure.mgmt.core import ARMPipelineClient
from msrest import Deserializer, Serializer

from . import models
from ._configuration import HealthcareApisManagementClientConfiguration
from .operations import DicomServicesOperations, FhirDestinationsOperations, FhirServicesOperations, IotConnectorFhirDestinationOperations, IotConnectorsOperations, OperationResultsOperations, Operations, PrivateEndpointConnectionsOperations, PrivateLinkResourcesOperations, ServicesOperations, WorkspacePrivateEndpointConnectionsOperations, WorkspacePrivateLinkResourcesOperations, WorkspacesOperations

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials import TokenCredential

class HealthcareApisManagementClient:
    """Azure Healthcare APIs Client.

    :ivar services: ServicesOperations operations
    :vartype services: azure.mgmt.healthcareapis.operations.ServicesOperations
    :ivar private_endpoint_connections: PrivateEndpointConnectionsOperations operations
    :vartype private_endpoint_connections:
     azure.mgmt.healthcareapis.operations.PrivateEndpointConnectionsOperations
    :ivar private_link_resources: PrivateLinkResourcesOperations operations
    :vartype private_link_resources:
     azure.mgmt.healthcareapis.operations.PrivateLinkResourcesOperations
    :ivar workspaces: WorkspacesOperations operations
    :vartype workspaces: azure.mgmt.healthcareapis.operations.WorkspacesOperations
    :ivar dicom_services: DicomServicesOperations operations
    :vartype dicom_services: azure.mgmt.healthcareapis.operations.DicomServicesOperations
    :ivar iot_connectors: IotConnectorsOperations operations
    :vartype iot_connectors: azure.mgmt.healthcareapis.operations.IotConnectorsOperations
    :ivar fhir_destinations: FhirDestinationsOperations operations
    :vartype fhir_destinations: azure.mgmt.healthcareapis.operations.FhirDestinationsOperations
    :ivar iot_connector_fhir_destination: IotConnectorFhirDestinationOperations operations
    :vartype iot_connector_fhir_destination:
     azure.mgmt.healthcareapis.operations.IotConnectorFhirDestinationOperations
    :ivar fhir_services: FhirServicesOperations operations
    :vartype fhir_services: azure.mgmt.healthcareapis.operations.FhirServicesOperations
    :ivar workspace_private_endpoint_connections: WorkspacePrivateEndpointConnectionsOperations
     operations
    :vartype workspace_private_endpoint_connections:
     azure.mgmt.healthcareapis.operations.WorkspacePrivateEndpointConnectionsOperations
    :ivar workspace_private_link_resources: WorkspacePrivateLinkResourcesOperations operations
    :vartype workspace_private_link_resources:
     azure.mgmt.healthcareapis.operations.WorkspacePrivateLinkResourcesOperations
    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.healthcareapis.operations.Operations
    :ivar operation_results: OperationResultsOperations operations
    :vartype operation_results: azure.mgmt.healthcareapis.operations.OperationResultsOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials.TokenCredential
    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :param base_url: Service URL. Default value is 'https://management.azure.com'.
    :type base_url: str
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
     Retry-After header is present.
    """

    def __init__(
        self,
        credential: "TokenCredential",
        subscription_id: str,
        base_url: str = "https://management.azure.com",
        **kwargs: Any
    ) -> None:
        self._config = HealthcareApisManagementClientConfiguration(credential=credential, subscription_id=subscription_id, **kwargs)
        self._client = ARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)
        self._serialize.client_side_validation = False
        self.services = ServicesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.private_endpoint_connections = PrivateEndpointConnectionsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.private_link_resources = PrivateLinkResourcesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.workspaces = WorkspacesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.dicom_services = DicomServicesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.iot_connectors = IotConnectorsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.fhir_destinations = FhirDestinationsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.iot_connector_fhir_destination = IotConnectorFhirDestinationOperations(self._client, self._config, self._serialize, self._deserialize)
        self.fhir_services = FhirServicesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.workspace_private_endpoint_connections = WorkspacePrivateEndpointConnectionsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.workspace_private_link_resources = WorkspacePrivateLinkResourcesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.operations = Operations(self._client, self._config, self._serialize, self._deserialize)
        self.operation_results = OperationResultsOperations(self._client, self._config, self._serialize, self._deserialize)


    def _send_request(
        self,
        request,  # type: HttpRequest
        **kwargs: Any
    ) -> HttpResponse:
        """Runs the network request through the client's chained policies.

        >>> from azure.core.rest import HttpRequest
        >>> request = HttpRequest("GET", "https://www.example.org/")
        <HttpRequest [GET], url: 'https://www.example.org/'>
        >>> response = client._send_request(request)
        <HttpResponse: 200 OK>

        For more information on this code flow, see https://aka.ms/azsdk/python/protocol/quickstart

        :param request: The network request you want to make. Required.
        :type request: ~azure.core.rest.HttpRequest
        :keyword bool stream: Whether the response payload will be streamed. Defaults to False.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~azure.core.rest.HttpResponse
        """

        request_copy = deepcopy(request)
        request_copy.url = self._client.format_url(request_copy.url)
        return self._client.send_request(request_copy, **kwargs)

    def close(self):
        # type: () -> None
        self._client.close()

    def __enter__(self):
        # type: () -> HealthcareApisManagementClient
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details):
        # type: (Any) -> None
        self._client.__exit__(*exc_details)
