# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from six import with_metaclass
from azure.core import CaseInsensitiveEnumMeta


class AdvancedFilterOperatorType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The operator type used for filtering, e.g., NumberIn, StringContains, BoolEquals and others.
    """

    NUMBER_IN = "NumberIn"
    NUMBER_NOT_IN = "NumberNotIn"
    NUMBER_LESS_THAN = "NumberLessThan"
    NUMBER_GREATER_THAN = "NumberGreaterThan"
    NUMBER_LESS_THAN_OR_EQUALS = "NumberLessThanOrEquals"
    NUMBER_GREATER_THAN_OR_EQUALS = "NumberGreaterThanOrEquals"
    BOOL_EQUALS = "BoolEquals"
    STRING_IN = "StringIn"
    STRING_NOT_IN = "StringNotIn"
    STRING_BEGINS_WITH = "StringBeginsWith"
    STRING_ENDS_WITH = "StringEndsWith"
    STRING_CONTAINS = "StringContains"
    NUMBER_IN_RANGE = "NumberInRange"
    NUMBER_NOT_IN_RANGE = "NumberNotInRange"
    STRING_NOT_BEGINS_WITH = "StringNotBeginsWith"
    STRING_NOT_ENDS_WITH = "StringNotEndsWith"
    STRING_NOT_CONTAINS = "StringNotContains"
    IS_NULL_OR_UNDEFINED = "IsNullOrUndefined"
    IS_NOT_NULL = "IsNotNull"

class ChannelProvisioningState(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Provisioning state of the channel.
    """

    CREATING = "Creating"
    UPDATING = "Updating"
    DELETING = "Deleting"
    SUCCEEDED = "Succeeded"
    CANCELED = "Canceled"
    FAILED = "Failed"

class ChannelType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The type of the event channel which represents the  direction flow of events.
    """

    PARTNER_TOPIC = "PartnerTopic"
    PARTNER_DESTINATION = "PartnerDestination"

class CreatedByType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The type of identity that created the resource.
    """

    USER = "User"
    APPLICATION = "Application"
    MANAGED_IDENTITY = "ManagedIdentity"
    KEY = "Key"

class DataResidencyBoundary(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Data Residency Boundary of the resource.
    """

    WITHIN_GEOPAIR = "WithinGeopair"
    WITHIN_REGION = "WithinRegion"

class DeadLetterEndPointType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Type of the endpoint for the dead letter destination
    """

    STORAGE_BLOB = "StorageBlob"

class DeliveryAttributeMappingType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Type of the delivery attribute or header name.
    """

    STATIC = "Static"
    DYNAMIC = "Dynamic"

class DomainProvisioningState(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Provisioning state of the Event Grid Domain Resource.
    """

    CREATING = "Creating"
    UPDATING = "Updating"
    DELETING = "Deleting"
    SUCCEEDED = "Succeeded"
    CANCELED = "Canceled"
    FAILED = "Failed"

class DomainTopicProvisioningState(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Provisioning state of the domain topic.
    """

    CREATING = "Creating"
    UPDATING = "Updating"
    DELETING = "Deleting"
    SUCCEEDED = "Succeeded"
    CANCELED = "Canceled"
    FAILED = "Failed"

class EndpointType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Type of the endpoint for the event subscription destination.
    """

    WEB_HOOK = "WebHook"
    EVENT_HUB = "EventHub"
    STORAGE_QUEUE = "StorageQueue"
    HYBRID_CONNECTION = "HybridConnection"
    SERVICE_BUS_QUEUE = "ServiceBusQueue"
    SERVICE_BUS_TOPIC = "ServiceBusTopic"
    AZURE_FUNCTION = "AzureFunction"
    PARTNER_DESTINATION = "PartnerDestination"

class EventChannelProvisioningState(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Provisioning state of the event channel.
    """

    CREATING = "Creating"
    UPDATING = "Updating"
    DELETING = "Deleting"
    SUCCEEDED = "Succeeded"
    CANCELED = "Canceled"
    FAILED = "Failed"

class EventDefinitionKind(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The kind of event type used.
    """

    INLINE = "Inline"

class EventDeliverySchema(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The event delivery schema for the event subscription.
    """

    EVENT_GRID_SCHEMA = "EventGridSchema"
    CUSTOM_INPUT_SCHEMA = "CustomInputSchema"
    CLOUD_EVENT_SCHEMA_V1_0 = "CloudEventSchemaV1_0"

class EventSubscriptionIdentityType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The type of managed identity used. The type 'SystemAssigned, UserAssigned' includes both an
    implicitly created identity and a set of user-assigned identities. The type 'None' will remove
    any identity.
    """

    SYSTEM_ASSIGNED = "SystemAssigned"
    USER_ASSIGNED = "UserAssigned"

class EventSubscriptionProvisioningState(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Provisioning state of the event subscription.
    """

    CREATING = "Creating"
    UPDATING = "Updating"
    DELETING = "Deleting"
    SUCCEEDED = "Succeeded"
    CANCELED = "Canceled"
    FAILED = "Failed"
    AWAITING_MANUAL_ACTION = "AwaitingManualAction"

class IdentityType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The type of managed identity used. The type 'SystemAssigned, UserAssigned' includes both an
    implicitly created identity and a set of user-assigned identities. The type 'None' will remove
    any identity.
    """

    NONE = "None"
    SYSTEM_ASSIGNED = "SystemAssigned"
    USER_ASSIGNED = "UserAssigned"
    SYSTEM_ASSIGNED_USER_ASSIGNED = "SystemAssigned, UserAssigned"

class InputSchema(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """This determines the format that Event Grid should expect for incoming events published to the
    Event Grid Domain Resource.
    """

    EVENT_GRID_SCHEMA = "EventGridSchema"
    CUSTOM_EVENT_SCHEMA = "CustomEventSchema"
    CLOUD_EVENT_SCHEMA_V1_0 = "CloudEventSchemaV1_0"

class InputSchemaMappingType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Type of the custom mapping
    """

    JSON = "Json"

class IpActionType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Action to perform based on the match or no match of the IpMask.
    """

    ALLOW = "Allow"

class ParentType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):

    TOPICS = "topics"
    DOMAINS = "domains"
    PARTNER_NAMESPACES = "partnerNamespaces"

class PartnerClientAuthenticationType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Type of client authentication
    """

    AZURE_AD = "AzureAD"

class PartnerConfigurationProvisioningState(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Provisioning state of the partner configuration.
    """

    CREATING = "Creating"
    UPDATING = "Updating"
    DELETING = "Deleting"
    SUCCEEDED = "Succeeded"
    CANCELED = "Canceled"
    FAILED = "Failed"

class PartnerDestinationActivationState(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Activation state of the partner destination.
    """

    NEVER_ACTIVATED = "NeverActivated"
    ACTIVATED = "Activated"

class PartnerDestinationProvisioningState(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Provisioning state of the partner destination.
    """

    CREATING = "Creating"
    UPDATING = "Updating"
    DELETING = "Deleting"
    SUCCEEDED = "Succeeded"
    CANCELED = "Canceled"
    FAILED = "Failed"

class PartnerEndpointType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Type of the endpoint for the partner destination
    """

    WEB_HOOK = "WebHook"

class PartnerNamespaceProvisioningState(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Provisioning state of the partner namespace.
    """

    CREATING = "Creating"
    UPDATING = "Updating"
    DELETING = "Deleting"
    SUCCEEDED = "Succeeded"
    CANCELED = "Canceled"
    FAILED = "Failed"

class PartnerRegistrationProvisioningState(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Provisioning state of the partner registration.
    """

    CREATING = "Creating"
    UPDATING = "Updating"
    DELETING = "Deleting"
    SUCCEEDED = "Succeeded"
    CANCELED = "Canceled"
    FAILED = "Failed"

class PartnerRegistrationVisibilityState(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Visibility state of the partner registration.
    """

    HIDDEN = "Hidden"
    PUBLIC_PREVIEW = "PublicPreview"
    GENERALLY_AVAILABLE = "GenerallyAvailable"

class PartnerTopicActivationState(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Activation state of the partner topic.
    """

    NEVER_ACTIVATED = "NeverActivated"
    ACTIVATED = "Activated"
    DEACTIVATED = "Deactivated"

class PartnerTopicProvisioningState(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Provisioning state of the partner topic.
    """

    CREATING = "Creating"
    UPDATING = "Updating"
    DELETING = "Deleting"
    SUCCEEDED = "Succeeded"
    CANCELED = "Canceled"
    FAILED = "Failed"

class PartnerTopicReadinessState(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The readiness state of the corresponding partner topic.
    """

    NOT_ACTIVATED_BY_USER_YET = "NotActivatedByUserYet"
    ACTIVATED_BY_USER = "ActivatedByUser"
    DEACTIVATED_BY_USER = "DeactivatedByUser"
    DELETED_BY_USER = "DeletedByUser"

class PartnerTopicRoutingMode(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """This determines if events published to this partner namespace should use the source attribute
    in the event payload
    or use the channel name in the header when matching to the partner topic. If none is specified,
    source attribute routing will be used to match the partner topic.
    """

    SOURCE_EVENT_ATTRIBUTE = "SourceEventAttribute"
    CHANNEL_NAME_HEADER = "ChannelNameHeader"

class PersistedConnectionStatus(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Status of the connection.
    """

    PENDING = "Pending"
    APPROVED = "Approved"
    REJECTED = "Rejected"
    DISCONNECTED = "Disconnected"

class PublicNetworkAccess(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """This determines if traffic is allowed over public network. By default it is enabled.
    You can further restrict to specific IPs by configuring :code:`<seealso
    cref="P:Microsoft.Azure.Events.ResourceProvider.Common.Contracts.DomainProperties.InboundIpRules"
    />`
    """

    ENABLED = "Enabled"
    DISABLED = "Disabled"

class ReadinessState(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The readiness state of the corresponding partner topic.
    """

    NEVER_ACTIVATED = "NeverActivated"
    ACTIVATED = "Activated"

class ResourceKind(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Kind of the resource.
    """

    AZURE = "Azure"
    AZURE_ARC = "AzureArc"

class ResourceProvisioningState(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Provisioning state of the Private Endpoint Connection.
    """

    CREATING = "Creating"
    UPDATING = "Updating"
    DELETING = "Deleting"
    SUCCEEDED = "Succeeded"
    CANCELED = "Canceled"
    FAILED = "Failed"

class ResourceRegionType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Region type of the resource.
    """

    REGIONAL_RESOURCE = "RegionalResource"
    GLOBAL_RESOURCE = "GlobalResource"

class Sku(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The Sku name of the resource. The possible values are: Basic or Premium.
    """

    BASIC = "Basic"
    PREMIUM = "Premium"

class TopicProvisioningState(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Provisioning state of the topic.
    """

    CREATING = "Creating"
    UPDATING = "Updating"
    DELETING = "Deleting"
    SUCCEEDED = "Succeeded"
    CANCELED = "Canceled"
    FAILED = "Failed"

class TopicTypePropertiesSupportedScopesForSourceItem(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):

    RESOURCE = "Resource"
    RESOURCE_GROUP = "ResourceGroup"
    AZURE_SUBSCRIPTION = "AzureSubscription"
    MANAGEMENT_GROUP = "ManagementGroup"

class TopicTypeProvisioningState(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Provisioning state of the topic type
    """

    CREATING = "Creating"
    UPDATING = "Updating"
    DELETING = "Deleting"
    SUCCEEDED = "Succeeded"
    CANCELED = "Canceled"
    FAILED = "Failed"

class VerifiedPartnerProvisioningState(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Provisioning state of the verified partner.
    """

    CREATING = "Creating"
    UPDATING = "Updating"
    DELETING = "Deleting"
    SUCCEEDED = "Succeeded"
    CANCELED = "Canceled"
    FAILED = "Failed"
