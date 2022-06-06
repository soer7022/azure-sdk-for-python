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


class AccessControlEntryAction(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Action object.
    """

    PERMIT = "Permit"
    DENY = "Deny"

class AppServiceCertificateOrderPatchResourcePropertiesAppServiceCertificateNotRenewableReasonsItem(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):

    REGISTRATION_STATUS_NOT_SUPPORTED_FOR_RENEWAL = "RegistrationStatusNotSupportedForRenewal"
    EXPIRATION_NOT_IN_RENEWAL_TIME_RANGE = "ExpirationNotInRenewalTimeRange"
    SUBSCRIPTION_NOT_ACTIVE = "SubscriptionNotActive"

class AppServiceCertificateOrderPropertiesAppServiceCertificateNotRenewableReasonsItem(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):

    REGISTRATION_STATUS_NOT_SUPPORTED_FOR_RENEWAL = "RegistrationStatusNotSupportedForRenewal"
    EXPIRATION_NOT_IN_RENEWAL_TIME_RANGE = "ExpirationNotInRenewalTimeRange"
    SUBSCRIPTION_NOT_ACTIVE = "SubscriptionNotActive"

class AppServicePlanRestrictions(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """App Service plans this offer is restricted to.
    """

    NONE = "None"
    FREE = "Free"
    SHARED = "Shared"
    BASIC = "Basic"
    STANDARD = "Standard"
    PREMIUM = "Premium"

class AutoHealActionType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Predefined action to be taken.
    """

    RECYCLE = "Recycle"
    LOG_EVENT = "LogEvent"
    CUSTOM_ACTION = "CustomAction"

class AzureResourceType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Type of the Azure resource the hostname is assigned to.
    """

    WEBSITE = "Website"
    TRAFFIC_MANAGER = "TrafficManager"

class AzureStorageState(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """State of the storage account.
    """

    OK = "Ok"
    INVALID_CREDENTIALS = "InvalidCredentials"
    INVALID_SHARE = "InvalidShare"

class AzureStorageType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Type of storage.
    """

    AZURE_FILES = "AzureFiles"
    AZURE_BLOB = "AzureBlob"

class BackupItemStatus(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Backup status.
    """

    IN_PROGRESS = "InProgress"
    FAILED = "Failed"
    SUCCEEDED = "Succeeded"
    TIMED_OUT = "TimedOut"
    CREATED = "Created"
    SKIPPED = "Skipped"
    PARTIALLY_SUCCEEDED = "PartiallySucceeded"
    DELETE_IN_PROGRESS = "DeleteInProgress"
    DELETE_FAILED = "DeleteFailed"
    DELETED = "Deleted"

class BackupRestoreOperationType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Operation type.
    """

    DEFAULT = "Default"
    CLONE = "Clone"
    RELOCATION = "Relocation"
    SNAPSHOT = "Snapshot"
    CLOUD_FS = "CloudFS"

class BuildStatus(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The status of the static site build.
    """

    WAITING_FOR_DEPLOYMENT = "WaitingForDeployment"
    UPLOADING = "Uploading"
    DEPLOYING = "Deploying"
    READY = "Ready"
    FAILED = "Failed"
    DELETING = "Deleting"
    DETACHED = "Detached"

class BuiltInAuthenticationProvider(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The default authentication provider to use when multiple providers are configured.
    This setting is only needed if multiple providers are configured and the unauthenticated client
    action is set to "RedirectToLoginPage".
    """

    AZURE_ACTIVE_DIRECTORY = "AzureActiveDirectory"
    FACEBOOK = "Facebook"
    GOOGLE = "Google"
    MICROSOFT_ACCOUNT = "MicrosoftAccount"
    TWITTER = "Twitter"
    GITHUB = "Github"

class CertificateOrderActionType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Action type.
    """

    CERTIFICATE_ISSUED = "CertificateIssued"
    CERTIFICATE_ORDER_CANCELED = "CertificateOrderCanceled"
    CERTIFICATE_ORDER_CREATED = "CertificateOrderCreated"
    CERTIFICATE_REVOKED = "CertificateRevoked"
    DOMAIN_VALIDATION_COMPLETE = "DomainValidationComplete"
    FRAUD_DETECTED = "FraudDetected"
    ORG_NAME_CHANGE = "OrgNameChange"
    ORG_VALIDATION_COMPLETE = "OrgValidationComplete"
    SAN_DROP = "SanDrop"
    FRAUD_CLEARED = "FraudCleared"
    CERTIFICATE_EXPIRED = "CertificateExpired"
    CERTIFICATE_EXPIRATION_WARNING = "CertificateExpirationWarning"
    FRAUD_DOCUMENTATION_REQUIRED = "FraudDocumentationRequired"
    UNKNOWN = "Unknown"

class CertificateOrderStatus(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Current order status.
    """

    PENDINGISSUANCE = "Pendingissuance"
    ISSUED = "Issued"
    REVOKED = "Revoked"
    CANCELED = "Canceled"
    DENIED = "Denied"
    PENDINGREVOCATION = "Pendingrevocation"
    PENDING_REKEY = "PendingRekey"
    UNUSED = "Unused"
    EXPIRED = "Expired"
    NOT_SUBMITTED = "NotSubmitted"

class CertificateProductType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Certificate product type.
    """

    STANDARD_DOMAIN_VALIDATED_SSL = "StandardDomainValidatedSsl"
    STANDARD_DOMAIN_VALIDATED_WILD_CARD_SSL = "StandardDomainValidatedWildCardSsl"

class Channels(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """List of channels that this recommendation can apply.
    """

    NOTIFICATION = "Notification"
    API = "Api"
    EMAIL = "Email"
    WEBHOOK = "Webhook"
    ALL = "All"

class CheckNameResourceTypes(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Resource type used for verification.
    """

    SITE = "Site"
    SLOT = "Slot"
    HOSTING_ENVIRONMENT = "HostingEnvironment"
    PUBLISHING_USER = "PublishingUser"
    MICROSOFT_WEB_SITES = "Microsoft.Web/sites"
    MICROSOFT_WEB_SITES_SLOTS = "Microsoft.Web/sites/slots"
    MICROSOFT_WEB_HOSTING_ENVIRONMENTS = "Microsoft.Web/hostingEnvironments"
    MICROSOFT_WEB_PUBLISHING_USERS = "Microsoft.Web/publishingUsers"

class ClientCertMode(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """This composes with ClientCertEnabled setting.
    
    
    * ClientCertEnabled: false means ClientCert is ignored.
    * ClientCertEnabled: true and ClientCertMode: Required means ClientCert is required.
    * ClientCertEnabled: true and ClientCertMode: Optional means ClientCert is optional or
    accepted.
    """

    REQUIRED = "Required"
    OPTIONAL = "Optional"

class CloneAbilityResult(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Name of app.
    """

    CLONEABLE = "Cloneable"
    PARTIALLY_CLONEABLE = "PartiallyCloneable"
    NOT_CLONEABLE = "NotCloneable"

class ComputeModeOptions(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Shared/dedicated workers.
    """

    SHARED = "Shared"
    DEDICATED = "Dedicated"
    DYNAMIC = "Dynamic"

class ConnectionStringType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Type of database.
    """

    MY_SQL = "MySql"
    SQL_SERVER = "SQLServer"
    SQL_AZURE = "SQLAzure"
    CUSTOM = "Custom"
    NOTIFICATION_HUB = "NotificationHub"
    SERVICE_BUS = "ServiceBus"
    EVENT_HUB = "EventHub"
    API_HUB = "ApiHub"
    DOC_DB = "DocDb"
    REDIS_CACHE = "RedisCache"
    POSTGRE_SQL = "PostgreSQL"

class ContinuousWebJobStatus(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Job status.
    """

    INITIALIZING = "Initializing"
    STARTING = "Starting"
    RUNNING = "Running"
    PENDING_RESTART = "PendingRestart"
    STOPPED = "Stopped"

class CookieExpirationConvention(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):

    FIXED_TIME = "FixedTime"
    IDENTITY_PROVIDER_DERIVED = "IdentityProviderDerived"

class CustomHostNameDnsRecordType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Type of the DNS record.
    """

    C_NAME = "CName"
    A = "A"

class DatabaseType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Database type (e.g. SqlAzure / MySql).
    """

    SQL_AZURE = "SqlAzure"
    MY_SQL = "MySql"
    LOCAL_MY_SQL = "LocalMySql"
    POSTGRE_SQL = "PostgreSql"

class DnsType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Current DNS type
    """

    AZURE_DNS = "AzureDns"
    DEFAULT_DOMAIN_REGISTRAR_DNS = "DefaultDomainRegistrarDns"

class DnsVerificationTestResult(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """DNS verification test result.
    """

    PASSED = "Passed"
    FAILED = "Failed"
    SKIPPED = "Skipped"

class DomainPatchResourcePropertiesDomainNotRenewableReasonsItem(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):

    REGISTRATION_STATUS_NOT_SUPPORTED_FOR_RENEWAL = "RegistrationStatusNotSupportedForRenewal"
    EXPIRATION_NOT_IN_RENEWAL_TIME_RANGE = "ExpirationNotInRenewalTimeRange"
    SUBSCRIPTION_NOT_ACTIVE = "SubscriptionNotActive"

class DomainPropertiesDomainNotRenewableReasonsItem(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):

    REGISTRATION_STATUS_NOT_SUPPORTED_FOR_RENEWAL = "RegistrationStatusNotSupportedForRenewal"
    EXPIRATION_NOT_IN_RENEWAL_TIME_RANGE = "ExpirationNotInRenewalTimeRange"
    SUBSCRIPTION_NOT_ACTIVE = "SubscriptionNotActive"

class DomainStatus(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Domain registration status.
    """

    ACTIVE = "Active"
    AWAITING = "Awaiting"
    CANCELLED = "Cancelled"
    CONFISCATED = "Confiscated"
    DISABLED = "Disabled"
    EXCLUDED = "Excluded"
    EXPIRED = "Expired"
    FAILED = "Failed"
    HELD = "Held"
    LOCKED = "Locked"
    PARKED = "Parked"
    PENDING = "Pending"
    RESERVED = "Reserved"
    REVERTED = "Reverted"
    SUSPENDED = "Suspended"
    TRANSFERRED = "Transferred"
    UNKNOWN = "Unknown"
    UNLOCKED = "Unlocked"
    UNPARKED = "Unparked"
    UPDATED = "Updated"
    JSON_CONVERTER_FAILED = "JsonConverterFailed"

class DomainType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Valid values are Regular domain: Azure will charge the full price of domain registration,
    SoftDeleted: Purchasing this domain will simply restore it and this operation will not cost
    anything.
    """

    REGULAR = "Regular"
    SOFT_DELETED = "SoftDeleted"

class Enum4(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):

    WINDOWS = "Windows"
    LINUX = "Linux"
    WINDOWS_FUNCTIONS = "WindowsFunctions"
    LINUX_FUNCTIONS = "LinuxFunctions"

class Enum5(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):

    WINDOWS = "Windows"
    LINUX = "Linux"
    WINDOWS_FUNCTIONS = "WindowsFunctions"
    LINUX_FUNCTIONS = "LinuxFunctions"

class ForwardProxyConvention(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):

    NO_PROXY = "NoProxy"
    STANDARD = "Standard"
    CUSTOM = "Custom"

class FrequencyUnit(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The unit of time for how often the backup should be executed (e.g. for weekly backup, this
    should be set to Day and FrequencyInterval should be set to 7)
    """

    DAY = "Day"
    HOUR = "Hour"

class FtpsState(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """State of FTP / FTPS service
    """

    ALL_ALLOWED = "AllAllowed"
    FTPS_ONLY = "FtpsOnly"
    DISABLED = "Disabled"

class HostingEnvironmentStatus(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Current status of the App Service Environment.
    """

    PREPARING = "Preparing"
    READY = "Ready"
    SCALING = "Scaling"
    DELETING = "Deleting"

class HostNameType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Type of the hostname.
    """

    VERIFIED = "Verified"
    MANAGED = "Managed"

class HostType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Indicates whether the hostname is a standard or repository hostname.
    """

    STANDARD = "Standard"
    REPOSITORY = "Repository"

class InAvailabilityReasonType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """:code:`<code>Invalid</code>` indicates the name provided does not match Azure App Service
    naming requirements. :code:`<code>AlreadyExists</code>` indicates that the name is already in
    use and is therefore unavailable.
    """

    INVALID = "Invalid"
    ALREADY_EXISTS = "AlreadyExists"

class IpFilterTag(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Defines what this IP filter will be used for. This is to support IP filtering on proxies.
    """

    DEFAULT = "Default"
    XFF_PROXY = "XffProxy"
    SERVICE_TAG = "ServiceTag"

class IssueType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Represents the type of the Detector
    """

    SERVICE_INCIDENT = "ServiceIncident"
    APP_DEPLOYMENT = "AppDeployment"
    APP_CRASH = "AppCrash"
    RUNTIME_ISSUE_DETECTED = "RuntimeIssueDetected"
    ASE_DEPLOYMENT = "AseDeployment"
    USER_ISSUE = "UserIssue"
    PLATFORM_ISSUE = "PlatformIssue"
    OTHER = "Other"

class KeyVaultSecretStatus(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Status of the Key Vault secret.
    """

    INITIALIZED = "Initialized"
    WAITING_ON_CERTIFICATE_ORDER = "WaitingOnCertificateOrder"
    SUCCEEDED = "Succeeded"
    CERTIFICATE_ORDER_FAILED = "CertificateOrderFailed"
    OPERATION_NOT_PERMITTED_ON_KEY_VAULT = "OperationNotPermittedOnKeyVault"
    AZURE_SERVICE_UNAUTHORIZED_TO_ACCESS_KEY_VAULT = "AzureServiceUnauthorizedToAccessKeyVault"
    KEY_VAULT_DOES_NOT_EXIST = "KeyVaultDoesNotExist"
    KEY_VAULT_SECRET_DOES_NOT_EXIST = "KeyVaultSecretDoesNotExist"
    UNKNOWN_ERROR = "UnknownError"
    EXTERNAL_PRIVATE_KEY = "ExternalPrivateKey"
    UNKNOWN = "Unknown"

class LoadBalancingMode(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Specifies which endpoints to serve internally in the Virtual Network for the App Service
    Environment.
    """

    NONE = "None"
    WEB = "Web"
    PUBLISHING = "Publishing"
    WEB_PUBLISHING = "Web,Publishing"

class LogLevel(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Log level.
    """

    OFF = "Off"
    VERBOSE = "Verbose"
    INFORMATION = "Information"
    WARNING = "Warning"
    ERROR = "Error"

class ManagedPipelineMode(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Managed pipeline mode.
    """

    INTEGRATED = "Integrated"
    CLASSIC = "Classic"

class ManagedServiceIdentityType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Type of managed service identity.
    """

    SYSTEM_ASSIGNED = "SystemAssigned"
    USER_ASSIGNED = "UserAssigned"
    SYSTEM_ASSIGNED_USER_ASSIGNED = "SystemAssigned, UserAssigned"
    NONE = "None"

class MSDeployLogEntryType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Log entry type
    """

    MESSAGE = "Message"
    WARNING = "Warning"
    ERROR = "Error"

class MSDeployProvisioningState(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Provisioning state
    """

    ACCEPTED = "accepted"
    RUNNING = "running"
    SUCCEEDED = "succeeded"
    FAILED = "failed"
    CANCELED = "canceled"

class MySqlMigrationType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The type of migration operation to be done
    """

    LOCAL_TO_REMOTE = "LocalToRemote"
    REMOTE_TO_LOCAL = "RemoteToLocal"

class NotificationLevel(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Level indicating how critical this recommendation can impact.
    """

    CRITICAL = "Critical"
    WARNING = "Warning"
    INFORMATION = "Information"
    NON_URGENT_SUGGESTION = "NonUrgentSuggestion"

class OperationStatus(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The current status of the operation.
    """

    IN_PROGRESS = "InProgress"
    FAILED = "Failed"
    SUCCEEDED = "Succeeded"
    TIMED_OUT = "TimedOut"
    CREATED = "Created"

class ProvisioningState(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Status of certificate order.
    """

    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    CANCELED = "Canceled"
    IN_PROGRESS = "InProgress"
    DELETING = "Deleting"

class PublicCertificateLocation(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Public Certificate Location
    """

    CURRENT_USER_MY = "CurrentUserMy"
    LOCAL_MACHINE_MY = "LocalMachineMy"
    UNKNOWN = "Unknown"

class PublishingProfileFormat(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Name of the format. Valid values are:
    FileZilla3
    WebDeploy -- default
    Ftp
    """

    FILE_ZILLA3 = "FileZilla3"
    WEB_DEPLOY = "WebDeploy"
    FTP = "Ftp"

class RedundancyMode(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Site redundancy mode
    """

    NONE = "None"
    MANUAL = "Manual"
    FAILOVER = "Failover"
    ACTIVE_ACTIVE = "ActiveActive"
    GEO_REDUNDANT = "GeoRedundant"

class RenderingType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Rendering Type
    """

    NO_GRAPH = "NoGraph"
    TABLE = "Table"
    TIME_SERIES = "TimeSeries"
    TIME_SERIES_PER_INSTANCE = "TimeSeriesPerInstance"

class ResourceScopeType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Name of a resource type this recommendation applies, e.g. Subscription, ServerFarm, Site.
    """

    SERVER_FARM = "ServerFarm"
    SUBSCRIPTION = "Subscription"
    WEB_SITE = "WebSite"

class RouteType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The type of route this is:
    DEFAULT - By default, every app has routes to the local address ranges specified by RFC1918
    INHERITED - Routes inherited from the real Virtual Network routes
    STATIC - Static route set on the app only
    
    These values will be used for syncing an app's routes with those from a Virtual Network.
    """

    DEFAULT = "DEFAULT"
    INHERITED = "INHERITED"
    STATIC = "STATIC"

class ScmType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """SCM type.
    """

    NONE = "None"
    DROPBOX = "Dropbox"
    TFS = "Tfs"
    LOCAL_GIT = "LocalGit"
    GIT_HUB = "GitHub"
    CODE_PLEX_GIT = "CodePlexGit"
    CODE_PLEX_HG = "CodePlexHg"
    BITBUCKET_GIT = "BitbucketGit"
    BITBUCKET_HG = "BitbucketHg"
    EXTERNAL_GIT = "ExternalGit"
    EXTERNAL_HG = "ExternalHg"
    ONE_DRIVE = "OneDrive"
    VSO = "VSO"
    VSTSRM = "VSTSRM"

class SiteAvailabilityState(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Management information availability state for the app.
    """

    NORMAL = "Normal"
    LIMITED = "Limited"
    DISASTER_RECOVERY_MODE = "DisasterRecoveryMode"

class SiteExtensionType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Site extension type.
    """

    GALLERY = "Gallery"
    WEB_ROOT = "WebRoot"

class SiteLoadBalancing(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Site load balancing.
    """

    WEIGHTED_ROUND_ROBIN = "WeightedRoundRobin"
    LEAST_REQUESTS = "LeastRequests"
    LEAST_RESPONSE_TIME = "LeastResponseTime"
    WEIGHTED_TOTAL_TRAFFIC = "WeightedTotalTraffic"
    REQUEST_HASH = "RequestHash"

class SiteRuntimeState(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):

    READY = "READY"
    STOPPED = "STOPPED"
    UNKNOWN = "UNKNOWN"

class SkuName(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):

    FREE = "Free"
    SHARED = "Shared"
    BASIC = "Basic"
    STANDARD = "Standard"
    PREMIUM = "Premium"
    DYNAMIC = "Dynamic"
    ISOLATED = "Isolated"
    PREMIUM_V2 = "PremiumV2"
    ELASTIC_PREMIUM = "ElasticPremium"
    ELASTIC_ISOLATED = "ElasticIsolated"

class SolutionType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Type of Solution
    """

    QUICK_SOLUTION = "QuickSolution"
    DEEP_INVESTIGATION = "DeepInvestigation"
    BEST_PRACTICES = "BestPractices"

class SslState(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """SSL type.
    """

    DISABLED = "Disabled"
    SNI_ENABLED = "SniEnabled"
    IP_BASED_ENABLED = "IpBasedEnabled"

class StatusOptions(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """App Service plan status.
    """

    READY = "Ready"
    PENDING = "Pending"
    CREATING = "Creating"

class SupportedTlsVersions(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """MinTlsVersion: configures the minimum version of TLS required for SSL requests
    """

    ONE0 = "1.0"
    ONE1 = "1.1"
    ONE2 = "1.2"

class TriggeredWebJobStatus(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Job status.
    """

    SUCCESS = "Success"
    FAILED = "Failed"
    ERROR = "Error"

class TriggerTypes(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The trigger type of the function
    """

    HTTP_TRIGGER = "HttpTrigger"
    UNKNOWN = "Unknown"

class UnauthenticatedClientAction(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The action to take when an unauthenticated client attempts to access the app.
    """

    REDIRECT_TO_LOGIN_PAGE = "RedirectToLoginPage"
    ALLOW_ANONYMOUS = "AllowAnonymous"

class UnauthenticatedClientActionV2(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):

    REDIRECT_TO_LOGIN_PAGE = "RedirectToLoginPage"
    ALLOW_ANONYMOUS = "AllowAnonymous"
    RETURN401 = "Return401"
    RETURN403 = "Return403"

class UsageState(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """State indicating whether the app has exceeded its quota usage. Read-only.
    """

    NORMAL = "Normal"
    EXCEEDED = "Exceeded"

class ValidateResourceTypes(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Resource type used for verification.
    """

    SERVER_FARM = "ServerFarm"
    SITE = "Site"

class WebJobType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Job type.
    """

    CONTINUOUS = "Continuous"
    TRIGGERED = "Triggered"

class WorkerSizeOptions(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Size of the machines.
    """

    SMALL = "Small"
    MEDIUM = "Medium"
    LARGE = "Large"
    D1 = "D1"
    D2 = "D2"
    D3 = "D3"
    NESTED_SMALL = "NestedSmall"
    DEFAULT = "Default"
