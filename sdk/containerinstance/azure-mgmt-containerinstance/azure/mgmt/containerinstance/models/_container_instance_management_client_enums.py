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


class AutoGeneratedDomainNameLabelScope(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The value representing the security enum.
    """

    UNSECURE = "Unsecure"
    TENANT_REUSE = "TenantReuse"
    SUBSCRIPTION_REUSE = "SubscriptionReuse"
    RESOURCE_GROUP_REUSE = "ResourceGroupReuse"
    NOREUSE = "Noreuse"

class ContainerGroupIpAddressType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Specifies if the IP is exposed to the public internet or private VNET.
    """

    PUBLIC = "Public"
    PRIVATE = "Private"

class ContainerGroupNetworkProtocol(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The protocol associated with the port.
    """

    TCP = "TCP"
    UDP = "UDP"

class ContainerGroupRestartPolicy(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Restart policy for all containers within the container group.
    
    
    * ``Always`` Always restart
    * ``OnFailure`` Restart on failure
    * ``Never`` Never restart
    """

    ALWAYS = "Always"
    ON_FAILURE = "OnFailure"
    NEVER = "Never"

class ContainerGroupSku(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The container group SKU.
    """

    STANDARD = "Standard"
    DEDICATED = "Dedicated"

class ContainerInstanceOperationsOrigin(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The intended executor of the operation.
    """

    USER = "User"
    SYSTEM = "System"

class ContainerNetworkProtocol(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The protocol associated with the port.
    """

    TCP = "TCP"
    UDP = "UDP"

class GpuSku(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The SKU of the GPU resource.
    """

    K80 = "K80"
    P100 = "P100"
    V100 = "V100"

class LogAnalyticsLogType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The log type to be used.
    """

    CONTAINER_INSIGHTS = "ContainerInsights"
    CONTAINER_INSTANCE_LOGS = "ContainerInstanceLogs"

class OperatingSystemTypes(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The operating system type required by the containers in the container group.
    """

    WINDOWS = "Windows"
    LINUX = "Linux"

class ResourceIdentityType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The type of identity used for the container group. The type 'SystemAssigned, UserAssigned'
    includes both an implicitly created identity and a set of user assigned identities. The type
    'None' will remove any identities from the container group.
    """

    SYSTEM_ASSIGNED = "SystemAssigned"
    USER_ASSIGNED = "UserAssigned"
    SYSTEM_ASSIGNED_USER_ASSIGNED = "SystemAssigned, UserAssigned"
    NONE = "None"

class Scheme(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The scheme.
    """

    HTTP = "http"
    HTTPS = "https"
