# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._models_py3 import AttachedDatabaseConfiguration
from ._models_py3 import AttachedDatabaseConfigurationListResult
from ._models_py3 import AutoPauseProperties
from ._models_py3 import AutoScaleProperties
from ._models_py3 import AvailableRpOperation
from ._models_py3 import AvailableRpOperationDisplayInfo
from ._models_py3 import AzureADOnlyAuthentication
from ._models_py3 import AzureADOnlyAuthenticationListResult
from ._models_py3 import AzureCapacity
from ._models_py3 import AzureEntityResource
from ._models_py3 import AzureResourceSku
from ._models_py3 import AzureSku
from ._models_py3 import BigDataPoolPatchInfo
from ._models_py3 import BigDataPoolResourceInfo
from ._models_py3 import BigDataPoolResourceInfoListResult
from ._models_py3 import CheckNameAvailabilityRequest
from ._models_py3 import CheckNameAvailabilityResponse
from ._models_py3 import CheckNameResult
from ._models_py3 import ClusterPrincipalAssignment
from ._models_py3 import ClusterPrincipalAssignmentCheckNameRequest
from ._models_py3 import ClusterPrincipalAssignmentListResult
from ._models_py3 import CmdkeySetup
from ._models_py3 import ComponentSetup
from ._models_py3 import CreateSqlPoolRestorePointDefinition
from ._models_py3 import CspWorkspaceAdminProperties
from ._models_py3 import CustomSetupBase
from ._models_py3 import CustomerManagedKeyDetails
from ._models_py3 import DataConnection
from ._models_py3 import DataConnectionCheckNameRequest
from ._models_py3 import DataConnectionListResult
from ._models_py3 import DataConnectionValidation
from ._models_py3 import DataConnectionValidationListResult
from ._models_py3 import DataConnectionValidationResult
from ._models_py3 import DataLakeStorageAccountDetails
from ._models_py3 import DataMaskingPolicy
from ._models_py3 import DataMaskingRule
from ._models_py3 import DataMaskingRuleListResult
from ._models_py3 import DataWarehouseUserActivities
from ._models_py3 import Database
from ._models_py3 import DatabaseCheckNameRequest
from ._models_py3 import DatabaseListResult
from ._models_py3 import DatabasePrincipalAssignment
from ._models_py3 import DatabasePrincipalAssignmentCheckNameRequest
from ._models_py3 import DatabasePrincipalAssignmentListResult
from ._models_py3 import DatabaseStatistics
from ._models_py3 import DedicatedSQLminimalTlsSettings
from ._models_py3 import DedicatedSQLminimalTlsSettingsListResult
from ._models_py3 import DedicatedSQLminimalTlsSettingsPatchInfo
from ._models_py3 import DynamicExecutorAllocation
from ._models_py3 import EncryptionDetails
from ._models_py3 import EncryptionProtector
from ._models_py3 import EncryptionProtectorListResult
from ._models_py3 import EntityReference
from ._models_py3 import EnvironmentVariableSetup
from ._models_py3 import ErrorAdditionalInfo
from ._models_py3 import ErrorDetail
from ._models_py3 import ErrorResponse
from ._models_py3 import EventGridDataConnection
from ._models_py3 import EventHubDataConnection
from ._models_py3 import ExtendedServerBlobAuditingPolicy
from ._models_py3 import ExtendedServerBlobAuditingPolicyListResult
from ._models_py3 import ExtendedSqlPoolBlobAuditingPolicy
from ._models_py3 import ExtendedSqlPoolBlobAuditingPolicyListResult
from ._models_py3 import FollowerDatabaseDefinition
from ._models_py3 import FollowerDatabaseListResult
from ._models_py3 import GeoBackupPolicy
from ._models_py3 import GeoBackupPolicyListResult
from ._models_py3 import GetSsisObjectMetadataRequest
from ._models_py3 import IntegrationRuntime
from ._models_py3 import IntegrationRuntimeAuthKeys
from ._models_py3 import IntegrationRuntimeComputeProperties
from ._models_py3 import IntegrationRuntimeConnectionInfo
from ._models_py3 import IntegrationRuntimeCustomSetupScriptProperties
from ._models_py3 import IntegrationRuntimeDataFlowProperties
from ._models_py3 import IntegrationRuntimeDataProxyProperties
from ._models_py3 import IntegrationRuntimeListResponse
from ._models_py3 import IntegrationRuntimeMonitoringData
from ._models_py3 import IntegrationRuntimeNodeIpAddress
from ._models_py3 import IntegrationRuntimeNodeMonitoringData
from ._models_py3 import IntegrationRuntimeOutboundNetworkDependenciesCategoryEndpoint
from ._models_py3 import IntegrationRuntimeOutboundNetworkDependenciesEndpoint
from ._models_py3 import IntegrationRuntimeOutboundNetworkDependenciesEndpointDetails
from ._models_py3 import IntegrationRuntimeOutboundNetworkDependenciesEndpointsResponse
from ._models_py3 import IntegrationRuntimeRegenerateKeyParameters
from ._models_py3 import IntegrationRuntimeResource
from ._models_py3 import IntegrationRuntimeSsisCatalogInfo
from ._models_py3 import IntegrationRuntimeSsisProperties
from ._models_py3 import IntegrationRuntimeStatus
from ._models_py3 import IntegrationRuntimeStatusResponse
from ._models_py3 import IntegrationRuntimeVNetProperties
from ._models_py3 import IotHubDataConnection
from ._models_py3 import IpFirewallRuleInfo
from ._models_py3 import IpFirewallRuleInfoListResult
from ._models_py3 import IpFirewallRuleProperties
from ._models_py3 import KekIdentityProperties
from ._models_py3 import Key
from ._models_py3 import KeyInfoListResult
from ._models_py3 import KustoPool
from ._models_py3 import KustoPoolCheckNameRequest
from ._models_py3 import KustoPoolListResult
from ._models_py3 import KustoPoolUpdate
from ._models_py3 import LanguageExtension
from ._models_py3 import LanguageExtensionsList
from ._models_py3 import LibraryInfo
from ._models_py3 import LibraryListResponse
from ._models_py3 import LibraryRequirements
from ._models_py3 import LibraryResource
from ._models_py3 import LinkedIntegrationRuntime
from ._models_py3 import LinkedIntegrationRuntimeKeyAuthorization
from ._models_py3 import LinkedIntegrationRuntimeRbacAuthorization
from ._models_py3 import LinkedIntegrationRuntimeType
from ._models_py3 import ListResourceSkusResult
from ._models_py3 import ListSqlPoolSecurityAlertPolicies
from ._models_py3 import MaintenanceWindowOptions
from ._models_py3 import MaintenanceWindowTimeRange
from ._models_py3 import MaintenanceWindows
from ._models_py3 import ManagedIdentity
from ._models_py3 import ManagedIdentitySqlControlSettingsModel
from ._models_py3 import ManagedIdentitySqlControlSettingsModelPropertiesGrantSqlControlToManagedIdentity
from ._models_py3 import ManagedIntegrationRuntime
from ._models_py3 import ManagedIntegrationRuntimeError
from ._models_py3 import ManagedIntegrationRuntimeNode
from ._models_py3 import ManagedIntegrationRuntimeOperationResult
from ._models_py3 import ManagedIntegrationRuntimeStatus
from ._models_py3 import ManagedVirtualNetworkSettings
from ._models_py3 import MetadataSyncConfig
from ._models_py3 import Operation
from ._models_py3 import OperationDisplay
from ._models_py3 import OperationListResult
from ._models_py3 import OperationMetaLogSpecification
from ._models_py3 import OperationMetaMetricDimensionSpecification
from ._models_py3 import OperationMetaMetricSpecification
from ._models_py3 import OperationMetaServiceSpecification
from ._models_py3 import OperationResource
from ._models_py3 import OptimizedAutoscale
from ._models_py3 import PrivateEndpoint
from ._models_py3 import PrivateEndpointConnection
from ._models_py3 import PrivateEndpointConnectionForPrivateLinkHub
from ._models_py3 import PrivateEndpointConnectionForPrivateLinkHubBasic
from ._models_py3 import PrivateEndpointConnectionForPrivateLinkHubBasicAutoGenerated
from ._models_py3 import PrivateEndpointConnectionForPrivateLinkHubResourceCollectionResponse
from ._models_py3 import PrivateEndpointConnectionList
from ._models_py3 import PrivateEndpointConnectionProperties
from ._models_py3 import PrivateLinkHub
from ._models_py3 import PrivateLinkHubInfoListResult
from ._models_py3 import PrivateLinkHubPatchInfo
from ._models_py3 import PrivateLinkResource
from ._models_py3 import PrivateLinkResourceListResult
from ._models_py3 import PrivateLinkResourceProperties
from ._models_py3 import PrivateLinkServiceConnectionState
from ._models_py3 import ProxyResource
from ._models_py3 import PurviewConfiguration
from ._models_py3 import QueryInterval
from ._models_py3 import QueryMetric
from ._models_py3 import QueryStatistic
from ._models_py3 import ReadOnlyFollowingDatabase
from ._models_py3 import ReadWriteDatabase
from ._models_py3 import RecommendedSensitivityLabelUpdate
from ._models_py3 import RecommendedSensitivityLabelUpdateList
from ._models_py3 import RecoverableSqlPool
from ._models_py3 import RecoverableSqlPoolListResult
from ._models_py3 import ReplaceAllFirewallRulesOperationResponse
from ._models_py3 import ReplaceAllIpFirewallRulesRequest
from ._models_py3 import ReplicationLink
from ._models_py3 import ReplicationLinkListResult
from ._models_py3 import Resource
from ._models_py3 import ResourceMoveDefinition
from ._models_py3 import RestorableDroppedSqlPool
from ._models_py3 import RestorableDroppedSqlPoolListResult
from ._models_py3 import RestorePoint
from ._models_py3 import RestorePointListResult
from ._models_py3 import SecretBase
from ._models_py3 import SecureString
from ._models_py3 import SelfHostedIntegrationRuntime
from ._models_py3 import SelfHostedIntegrationRuntimeNode
from ._models_py3 import SelfHostedIntegrationRuntimeStatus
from ._models_py3 import SensitivityLabel
from ._models_py3 import SensitivityLabelListResult
from ._models_py3 import SensitivityLabelUpdate
from ._models_py3 import SensitivityLabelUpdateList
from ._models_py3 import ServerBlobAuditingPolicy
from ._models_py3 import ServerBlobAuditingPolicyListResult
from ._models_py3 import ServerSecurityAlertPolicy
from ._models_py3 import ServerSecurityAlertPolicyListResult
from ._models_py3 import ServerUsage
from ._models_py3 import ServerUsageListResult
from ._models_py3 import ServerVulnerabilityAssessment
from ._models_py3 import ServerVulnerabilityAssessmentListResult
from ._models_py3 import Sku
from ._models_py3 import SkuDescription
from ._models_py3 import SkuDescriptionList
from ._models_py3 import SkuLocationInfoItem
from ._models_py3 import SparkConfigProperties
from ._models_py3 import SparkConfigurationListResponse
from ._models_py3 import SparkConfigurationResource
from ._models_py3 import SqlPool
from ._models_py3 import SqlPoolBlobAuditingPolicy
from ._models_py3 import SqlPoolBlobAuditingPolicyListResult
from ._models_py3 import SqlPoolBlobAuditingPolicySqlPoolOperationListResult
from ._models_py3 import SqlPoolColumn
from ._models_py3 import SqlPoolColumnListResult
from ._models_py3 import SqlPoolConnectionPolicy
from ._models_py3 import SqlPoolInfoListResult
from ._models_py3 import SqlPoolOperation
from ._models_py3 import SqlPoolPatchInfo
from ._models_py3 import SqlPoolSchema
from ._models_py3 import SqlPoolSchemaListResult
from ._models_py3 import SqlPoolSecurityAlertPolicy
from ._models_py3 import SqlPoolTable
from ._models_py3 import SqlPoolTableListResult
from ._models_py3 import SqlPoolUsage
from ._models_py3 import SqlPoolUsageListResult
from ._models_py3 import SqlPoolVulnerabilityAssessment
from ._models_py3 import SqlPoolVulnerabilityAssessmentListResult
from ._models_py3 import SqlPoolVulnerabilityAssessmentRuleBaseline
from ._models_py3 import SqlPoolVulnerabilityAssessmentRuleBaselineItem
from ._models_py3 import SqlPoolVulnerabilityAssessmentScansExport
from ._models_py3 import SsisEnvironment
from ._models_py3 import SsisEnvironmentReference
from ._models_py3 import SsisFolder
from ._models_py3 import SsisObjectMetadata
from ._models_py3 import SsisObjectMetadataListResponse
from ._models_py3 import SsisObjectMetadataStatusResponse
from ._models_py3 import SsisPackage
from ._models_py3 import SsisParameter
from ._models_py3 import SsisProject
from ._models_py3 import SsisVariable
from ._models_py3 import SubResource
from ._models_py3 import SystemData
from ._models_py3 import TableLevelSharingProperties
from ._models_py3 import TopQueries
from ._models_py3 import TopQueriesListResult
from ._models_py3 import TrackedResource
from ._models_py3 import TransparentDataEncryption
from ._models_py3 import TransparentDataEncryptionListResult
from ._models_py3 import UpdateIntegrationRuntimeNodeRequest
from ._models_py3 import UpdateIntegrationRuntimeRequest
from ._models_py3 import UserAssignedManagedIdentity
from ._models_py3 import VirtualNetworkProfile
from ._models_py3 import VulnerabilityAssessmentRecurringScansProperties
from ._models_py3 import VulnerabilityAssessmentScanError
from ._models_py3 import VulnerabilityAssessmentScanRecord
from ._models_py3 import VulnerabilityAssessmentScanRecordListResult
from ._models_py3 import WorkloadClassifier
from ._models_py3 import WorkloadClassifierListResult
from ._models_py3 import WorkloadGroup
from ._models_py3 import WorkloadGroupListResult
from ._models_py3 import Workspace
from ._models_py3 import WorkspaceAadAdminInfo
from ._models_py3 import WorkspaceInfoListResult
from ._models_py3 import WorkspaceKeyDetails
from ._models_py3 import WorkspacePatchInfo
from ._models_py3 import WorkspaceRepositoryConfiguration


from ._synapse_management_client_enums import (
    AzureADOnlyAuthenticationName,
    AzureScaleType,
    BlobAuditingPolicyName,
    BlobAuditingPolicyState,
    BlobStorageEventType,
    ClusterPrincipalRole,
    ColumnDataType,
    Compression,
    ConfigurationType,
    ConnectionPolicyName,
    CreateMode,
    CreatedByType,
    DataConnectionKind,
    DataFlowComputeType,
    DataMaskingFunction,
    DataMaskingRuleState,
    DataMaskingState,
    DataWarehouseUserActivityName,
    DatabasePrincipalRole,
    DayOfWeek,
    DedicatedSQLMinimalTlsSettingsName,
    DefaultPrincipalsModificationKind,
    EncryptionProtectorName,
    EventGridDataFormat,
    EventHubDataFormat,
    GeoBackupPolicyName,
    GeoBackupPolicyState,
    IntegrationRuntimeAuthKeyName,
    IntegrationRuntimeAutoUpdate,
    IntegrationRuntimeEdition,
    IntegrationRuntimeEntityReferenceType,
    IntegrationRuntimeInternalChannelEncryptionMode,
    IntegrationRuntimeLicenseType,
    IntegrationRuntimeSsisCatalogPricingTier,
    IntegrationRuntimeState,
    IntegrationRuntimeType,
    IntegrationRuntimeUpdateResult,
    IotHubDataFormat,
    Kind,
    LanguageExtensionName,
    ManagedIdentitySqlControlSettingsModelPropertiesGrantSqlControlToManagedIdentityActualState,
    ManagedIdentitySqlControlSettingsModelPropertiesGrantSqlControlToManagedIdentityDesiredState,
    ManagedIntegrationRuntimeNodeStatus,
    ManagementOperationState,
    NodeSize,
    NodeSizeFamily,
    OperationStatus,
    PrincipalType,
    PrincipalsModificationKind,
    ProvisioningState,
    QueryAggregationFunction,
    QueryExecutionType,
    QueryMetricUnit,
    QueryObservedMetricType,
    Reason,
    RecommendedSensitivityLabelUpdateKind,
    ReplicationRole,
    ReplicationState,
    ResourceIdentityType,
    ResourceProvisioningState,
    RestorePointType,
    SecurityAlertPolicyName,
    SecurityAlertPolicyNameAutoGenerated,
    SecurityAlertPolicyState,
    SelfHostedIntegrationRuntimeNodeStatus,
    SensitivityLabelRank,
    SensitivityLabelSource,
    SensitivityLabelUpdateKind,
    ServerKeyType,
    SkuName,
    SkuSize,
    SsisObjectMetadataType,
    State,
    StateValue,
    StorageAccountType,
    TransparentDataEncryptionName,
    TransparentDataEncryptionStatus,
    Type,
    VulnerabilityAssessmentName,
    VulnerabilityAssessmentPolicyBaselineName,
    VulnerabilityAssessmentScanState,
    VulnerabilityAssessmentScanTriggerType,
    WorkspacePublicNetworkAccess,
)

__all__ = [
    'AttachedDatabaseConfiguration',
    'AttachedDatabaseConfigurationListResult',
    'AutoPauseProperties',
    'AutoScaleProperties',
    'AvailableRpOperation',
    'AvailableRpOperationDisplayInfo',
    'AzureADOnlyAuthentication',
    'AzureADOnlyAuthenticationListResult',
    'AzureCapacity',
    'AzureEntityResource',
    'AzureResourceSku',
    'AzureSku',
    'BigDataPoolPatchInfo',
    'BigDataPoolResourceInfo',
    'BigDataPoolResourceInfoListResult',
    'CheckNameAvailabilityRequest',
    'CheckNameAvailabilityResponse',
    'CheckNameResult',
    'ClusterPrincipalAssignment',
    'ClusterPrincipalAssignmentCheckNameRequest',
    'ClusterPrincipalAssignmentListResult',
    'CmdkeySetup',
    'ComponentSetup',
    'CreateSqlPoolRestorePointDefinition',
    'CspWorkspaceAdminProperties',
    'CustomSetupBase',
    'CustomerManagedKeyDetails',
    'DataConnection',
    'DataConnectionCheckNameRequest',
    'DataConnectionListResult',
    'DataConnectionValidation',
    'DataConnectionValidationListResult',
    'DataConnectionValidationResult',
    'DataLakeStorageAccountDetails',
    'DataMaskingPolicy',
    'DataMaskingRule',
    'DataMaskingRuleListResult',
    'DataWarehouseUserActivities',
    'Database',
    'DatabaseCheckNameRequest',
    'DatabaseListResult',
    'DatabasePrincipalAssignment',
    'DatabasePrincipalAssignmentCheckNameRequest',
    'DatabasePrincipalAssignmentListResult',
    'DatabaseStatistics',
    'DedicatedSQLminimalTlsSettings',
    'DedicatedSQLminimalTlsSettingsListResult',
    'DedicatedSQLminimalTlsSettingsPatchInfo',
    'DynamicExecutorAllocation',
    'EncryptionDetails',
    'EncryptionProtector',
    'EncryptionProtectorListResult',
    'EntityReference',
    'EnvironmentVariableSetup',
    'ErrorAdditionalInfo',
    'ErrorDetail',
    'ErrorResponse',
    'EventGridDataConnection',
    'EventHubDataConnection',
    'ExtendedServerBlobAuditingPolicy',
    'ExtendedServerBlobAuditingPolicyListResult',
    'ExtendedSqlPoolBlobAuditingPolicy',
    'ExtendedSqlPoolBlobAuditingPolicyListResult',
    'FollowerDatabaseDefinition',
    'FollowerDatabaseListResult',
    'GeoBackupPolicy',
    'GeoBackupPolicyListResult',
    'GetSsisObjectMetadataRequest',
    'IntegrationRuntime',
    'IntegrationRuntimeAuthKeys',
    'IntegrationRuntimeComputeProperties',
    'IntegrationRuntimeConnectionInfo',
    'IntegrationRuntimeCustomSetupScriptProperties',
    'IntegrationRuntimeDataFlowProperties',
    'IntegrationRuntimeDataProxyProperties',
    'IntegrationRuntimeListResponse',
    'IntegrationRuntimeMonitoringData',
    'IntegrationRuntimeNodeIpAddress',
    'IntegrationRuntimeNodeMonitoringData',
    'IntegrationRuntimeOutboundNetworkDependenciesCategoryEndpoint',
    'IntegrationRuntimeOutboundNetworkDependenciesEndpoint',
    'IntegrationRuntimeOutboundNetworkDependenciesEndpointDetails',
    'IntegrationRuntimeOutboundNetworkDependenciesEndpointsResponse',
    'IntegrationRuntimeRegenerateKeyParameters',
    'IntegrationRuntimeResource',
    'IntegrationRuntimeSsisCatalogInfo',
    'IntegrationRuntimeSsisProperties',
    'IntegrationRuntimeStatus',
    'IntegrationRuntimeStatusResponse',
    'IntegrationRuntimeVNetProperties',
    'IotHubDataConnection',
    'IpFirewallRuleInfo',
    'IpFirewallRuleInfoListResult',
    'IpFirewallRuleProperties',
    'KekIdentityProperties',
    'Key',
    'KeyInfoListResult',
    'KustoPool',
    'KustoPoolCheckNameRequest',
    'KustoPoolListResult',
    'KustoPoolUpdate',
    'LanguageExtension',
    'LanguageExtensionsList',
    'LibraryInfo',
    'LibraryListResponse',
    'LibraryRequirements',
    'LibraryResource',
    'LinkedIntegrationRuntime',
    'LinkedIntegrationRuntimeKeyAuthorization',
    'LinkedIntegrationRuntimeRbacAuthorization',
    'LinkedIntegrationRuntimeType',
    'ListResourceSkusResult',
    'ListSqlPoolSecurityAlertPolicies',
    'MaintenanceWindowOptions',
    'MaintenanceWindowTimeRange',
    'MaintenanceWindows',
    'ManagedIdentity',
    'ManagedIdentitySqlControlSettingsModel',
    'ManagedIdentitySqlControlSettingsModelPropertiesGrantSqlControlToManagedIdentity',
    'ManagedIntegrationRuntime',
    'ManagedIntegrationRuntimeError',
    'ManagedIntegrationRuntimeNode',
    'ManagedIntegrationRuntimeOperationResult',
    'ManagedIntegrationRuntimeStatus',
    'ManagedVirtualNetworkSettings',
    'MetadataSyncConfig',
    'Operation',
    'OperationDisplay',
    'OperationListResult',
    'OperationMetaLogSpecification',
    'OperationMetaMetricDimensionSpecification',
    'OperationMetaMetricSpecification',
    'OperationMetaServiceSpecification',
    'OperationResource',
    'OptimizedAutoscale',
    'PrivateEndpoint',
    'PrivateEndpointConnection',
    'PrivateEndpointConnectionForPrivateLinkHub',
    'PrivateEndpointConnectionForPrivateLinkHubBasic',
    'PrivateEndpointConnectionForPrivateLinkHubBasicAutoGenerated',
    'PrivateEndpointConnectionForPrivateLinkHubResourceCollectionResponse',
    'PrivateEndpointConnectionList',
    'PrivateEndpointConnectionProperties',
    'PrivateLinkHub',
    'PrivateLinkHubInfoListResult',
    'PrivateLinkHubPatchInfo',
    'PrivateLinkResource',
    'PrivateLinkResourceListResult',
    'PrivateLinkResourceProperties',
    'PrivateLinkServiceConnectionState',
    'ProxyResource',
    'PurviewConfiguration',
    'QueryInterval',
    'QueryMetric',
    'QueryStatistic',
    'ReadOnlyFollowingDatabase',
    'ReadWriteDatabase',
    'RecommendedSensitivityLabelUpdate',
    'RecommendedSensitivityLabelUpdateList',
    'RecoverableSqlPool',
    'RecoverableSqlPoolListResult',
    'ReplaceAllFirewallRulesOperationResponse',
    'ReplaceAllIpFirewallRulesRequest',
    'ReplicationLink',
    'ReplicationLinkListResult',
    'Resource',
    'ResourceMoveDefinition',
    'RestorableDroppedSqlPool',
    'RestorableDroppedSqlPoolListResult',
    'RestorePoint',
    'RestorePointListResult',
    'SecretBase',
    'SecureString',
    'SelfHostedIntegrationRuntime',
    'SelfHostedIntegrationRuntimeNode',
    'SelfHostedIntegrationRuntimeStatus',
    'SensitivityLabel',
    'SensitivityLabelListResult',
    'SensitivityLabelUpdate',
    'SensitivityLabelUpdateList',
    'ServerBlobAuditingPolicy',
    'ServerBlobAuditingPolicyListResult',
    'ServerSecurityAlertPolicy',
    'ServerSecurityAlertPolicyListResult',
    'ServerUsage',
    'ServerUsageListResult',
    'ServerVulnerabilityAssessment',
    'ServerVulnerabilityAssessmentListResult',
    'Sku',
    'SkuDescription',
    'SkuDescriptionList',
    'SkuLocationInfoItem',
    'SparkConfigProperties',
    'SparkConfigurationListResponse',
    'SparkConfigurationResource',
    'SqlPool',
    'SqlPoolBlobAuditingPolicy',
    'SqlPoolBlobAuditingPolicyListResult',
    'SqlPoolBlobAuditingPolicySqlPoolOperationListResult',
    'SqlPoolColumn',
    'SqlPoolColumnListResult',
    'SqlPoolConnectionPolicy',
    'SqlPoolInfoListResult',
    'SqlPoolOperation',
    'SqlPoolPatchInfo',
    'SqlPoolSchema',
    'SqlPoolSchemaListResult',
    'SqlPoolSecurityAlertPolicy',
    'SqlPoolTable',
    'SqlPoolTableListResult',
    'SqlPoolUsage',
    'SqlPoolUsageListResult',
    'SqlPoolVulnerabilityAssessment',
    'SqlPoolVulnerabilityAssessmentListResult',
    'SqlPoolVulnerabilityAssessmentRuleBaseline',
    'SqlPoolVulnerabilityAssessmentRuleBaselineItem',
    'SqlPoolVulnerabilityAssessmentScansExport',
    'SsisEnvironment',
    'SsisEnvironmentReference',
    'SsisFolder',
    'SsisObjectMetadata',
    'SsisObjectMetadataListResponse',
    'SsisObjectMetadataStatusResponse',
    'SsisPackage',
    'SsisParameter',
    'SsisProject',
    'SsisVariable',
    'SubResource',
    'SystemData',
    'TableLevelSharingProperties',
    'TopQueries',
    'TopQueriesListResult',
    'TrackedResource',
    'TransparentDataEncryption',
    'TransparentDataEncryptionListResult',
    'UpdateIntegrationRuntimeNodeRequest',
    'UpdateIntegrationRuntimeRequest',
    'UserAssignedManagedIdentity',
    'VirtualNetworkProfile',
    'VulnerabilityAssessmentRecurringScansProperties',
    'VulnerabilityAssessmentScanError',
    'VulnerabilityAssessmentScanRecord',
    'VulnerabilityAssessmentScanRecordListResult',
    'WorkloadClassifier',
    'WorkloadClassifierListResult',
    'WorkloadGroup',
    'WorkloadGroupListResult',
    'Workspace',
    'WorkspaceAadAdminInfo',
    'WorkspaceInfoListResult',
    'WorkspaceKeyDetails',
    'WorkspacePatchInfo',
    'WorkspaceRepositoryConfiguration',
    'AzureADOnlyAuthenticationName',
    'AzureScaleType',
    'BlobAuditingPolicyName',
    'BlobAuditingPolicyState',
    'BlobStorageEventType',
    'ClusterPrincipalRole',
    'ColumnDataType',
    'Compression',
    'ConfigurationType',
    'ConnectionPolicyName',
    'CreateMode',
    'CreatedByType',
    'DataConnectionKind',
    'DataFlowComputeType',
    'DataMaskingFunction',
    'DataMaskingRuleState',
    'DataMaskingState',
    'DataWarehouseUserActivityName',
    'DatabasePrincipalRole',
    'DayOfWeek',
    'DedicatedSQLMinimalTlsSettingsName',
    'DefaultPrincipalsModificationKind',
    'EncryptionProtectorName',
    'EventGridDataFormat',
    'EventHubDataFormat',
    'GeoBackupPolicyName',
    'GeoBackupPolicyState',
    'IntegrationRuntimeAuthKeyName',
    'IntegrationRuntimeAutoUpdate',
    'IntegrationRuntimeEdition',
    'IntegrationRuntimeEntityReferenceType',
    'IntegrationRuntimeInternalChannelEncryptionMode',
    'IntegrationRuntimeLicenseType',
    'IntegrationRuntimeSsisCatalogPricingTier',
    'IntegrationRuntimeState',
    'IntegrationRuntimeType',
    'IntegrationRuntimeUpdateResult',
    'IotHubDataFormat',
    'Kind',
    'LanguageExtensionName',
    'ManagedIdentitySqlControlSettingsModelPropertiesGrantSqlControlToManagedIdentityActualState',
    'ManagedIdentitySqlControlSettingsModelPropertiesGrantSqlControlToManagedIdentityDesiredState',
    'ManagedIntegrationRuntimeNodeStatus',
    'ManagementOperationState',
    'NodeSize',
    'NodeSizeFamily',
    'OperationStatus',
    'PrincipalType',
    'PrincipalsModificationKind',
    'ProvisioningState',
    'QueryAggregationFunction',
    'QueryExecutionType',
    'QueryMetricUnit',
    'QueryObservedMetricType',
    'Reason',
    'RecommendedSensitivityLabelUpdateKind',
    'ReplicationRole',
    'ReplicationState',
    'ResourceIdentityType',
    'ResourceProvisioningState',
    'RestorePointType',
    'SecurityAlertPolicyName',
    'SecurityAlertPolicyNameAutoGenerated',
    'SecurityAlertPolicyState',
    'SelfHostedIntegrationRuntimeNodeStatus',
    'SensitivityLabelRank',
    'SensitivityLabelSource',
    'SensitivityLabelUpdateKind',
    'ServerKeyType',
    'SkuName',
    'SkuSize',
    'SsisObjectMetadataType',
    'State',
    'StateValue',
    'StorageAccountType',
    'TransparentDataEncryptionName',
    'TransparentDataEncryptionStatus',
    'Type',
    'VulnerabilityAssessmentName',
    'VulnerabilityAssessmentPolicyBaselineName',
    'VulnerabilityAssessmentScanState',
    'VulnerabilityAssessmentScanTriggerType',
    'WorkspacePublicNetworkAccess',
]
