# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, List, Optional, Union

import msrest.serialization

from ._policy_client_enums import *


class PolicyAssignment(msrest.serialization.Model):
    """The policy assignment.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: The ID of the policy assignment.
    :vartype id: str
    :ivar type: The type of the policy assignment.
    :vartype type: str
    :ivar name: The name of the policy assignment.
    :vartype name: str
    :ivar display_name: The display name of the policy assignment.
    :vartype display_name: str
    :ivar policy_definition_id: The ID of the policy definition.
    :vartype policy_definition_id: str
    :ivar scope: The scope for the policy assignment.
    :vartype scope: str
    :ivar parameters: Required if a parameter is used in policy rule.
    :vartype parameters: any
    :ivar description: This message will be part of response in case of policy violation.
    :vartype description: str
    """

    _validation = {
        'id': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'display_name': {'key': 'properties.displayName', 'type': 'str'},
        'policy_definition_id': {'key': 'properties.policyDefinitionId', 'type': 'str'},
        'scope': {'key': 'properties.scope', 'type': 'str'},
        'parameters': {'key': 'properties.parameters', 'type': 'object'},
        'description': {'key': 'properties.description', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        type: Optional[str] = None,
        name: Optional[str] = None,
        display_name: Optional[str] = None,
        policy_definition_id: Optional[str] = None,
        scope: Optional[str] = None,
        parameters: Optional[Any] = None,
        description: Optional[str] = None,
        **kwargs
    ):
        """
        :keyword type: The type of the policy assignment.
        :paramtype type: str
        :keyword name: The name of the policy assignment.
        :paramtype name: str
        :keyword display_name: The display name of the policy assignment.
        :paramtype display_name: str
        :keyword policy_definition_id: The ID of the policy definition.
        :paramtype policy_definition_id: str
        :keyword scope: The scope for the policy assignment.
        :paramtype scope: str
        :keyword parameters: Required if a parameter is used in policy rule.
        :paramtype parameters: any
        :keyword description: This message will be part of response in case of policy violation.
        :paramtype description: str
        """
        super(PolicyAssignment, self).__init__(**kwargs)
        self.id = None
        self.type = type
        self.name = name
        self.display_name = display_name
        self.policy_definition_id = policy_definition_id
        self.scope = scope
        self.parameters = parameters
        self.description = description


class PolicyAssignmentListResult(msrest.serialization.Model):
    """List of policy assignments.

    :ivar value: An array of policy assignments.
    :vartype value: list[~azure.mgmt.resource.policy.v2016_12_01.models.PolicyAssignment]
    :ivar next_link: The URL to use for getting the next set of results.
    :vartype next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[PolicyAssignment]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        value: Optional[List["PolicyAssignment"]] = None,
        next_link: Optional[str] = None,
        **kwargs
    ):
        """
        :keyword value: An array of policy assignments.
        :paramtype value: list[~azure.mgmt.resource.policy.v2016_12_01.models.PolicyAssignment]
        :keyword next_link: The URL to use for getting the next set of results.
        :paramtype next_link: str
        """
        super(PolicyAssignmentListResult, self).__init__(**kwargs)
        self.value = value
        self.next_link = next_link


class PolicyDefinition(msrest.serialization.Model):
    """The policy definition.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: The ID of the policy definition.
    :vartype id: str
    :ivar name: The name of the policy definition.
    :vartype name: str
    :ivar policy_type: The type of policy definition. Possible values are NotSpecified, BuiltIn,
     and Custom. Possible values include: "NotSpecified", "BuiltIn", "Custom".
    :vartype policy_type: str or ~azure.mgmt.resource.policy.v2016_12_01.models.PolicyType
    :ivar mode: The policy definition mode. Possible values are NotSpecified, Indexed, and All.
     Possible values include: "NotSpecified", "Indexed", "All".
    :vartype mode: str or ~azure.mgmt.resource.policy.v2016_12_01.models.PolicyMode
    :ivar display_name: The display name of the policy definition.
    :vartype display_name: str
    :ivar description: The policy definition description.
    :vartype description: str
    :ivar policy_rule: The policy rule.
    :vartype policy_rule: any
    :ivar metadata: The policy definition metadata.
    :vartype metadata: any
    :ivar parameters: Required if a parameter is used in policy rule.
    :vartype parameters: any
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'policy_type': {'key': 'properties.policyType', 'type': 'str'},
        'mode': {'key': 'properties.mode', 'type': 'str'},
        'display_name': {'key': 'properties.displayName', 'type': 'str'},
        'description': {'key': 'properties.description', 'type': 'str'},
        'policy_rule': {'key': 'properties.policyRule', 'type': 'object'},
        'metadata': {'key': 'properties.metadata', 'type': 'object'},
        'parameters': {'key': 'properties.parameters', 'type': 'object'},
    }

    def __init__(
        self,
        *,
        policy_type: Optional[Union[str, "PolicyType"]] = None,
        mode: Optional[Union[str, "PolicyMode"]] = None,
        display_name: Optional[str] = None,
        description: Optional[str] = None,
        policy_rule: Optional[Any] = None,
        metadata: Optional[Any] = None,
        parameters: Optional[Any] = None,
        **kwargs
    ):
        """
        :keyword policy_type: The type of policy definition. Possible values are NotSpecified, BuiltIn,
         and Custom. Possible values include: "NotSpecified", "BuiltIn", "Custom".
        :paramtype policy_type: str or ~azure.mgmt.resource.policy.v2016_12_01.models.PolicyType
        :keyword mode: The policy definition mode. Possible values are NotSpecified, Indexed, and All.
         Possible values include: "NotSpecified", "Indexed", "All".
        :paramtype mode: str or ~azure.mgmt.resource.policy.v2016_12_01.models.PolicyMode
        :keyword display_name: The display name of the policy definition.
        :paramtype display_name: str
        :keyword description: The policy definition description.
        :paramtype description: str
        :keyword policy_rule: The policy rule.
        :paramtype policy_rule: any
        :keyword metadata: The policy definition metadata.
        :paramtype metadata: any
        :keyword parameters: Required if a parameter is used in policy rule.
        :paramtype parameters: any
        """
        super(PolicyDefinition, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.policy_type = policy_type
        self.mode = mode
        self.display_name = display_name
        self.description = description
        self.policy_rule = policy_rule
        self.metadata = metadata
        self.parameters = parameters


class PolicyDefinitionListResult(msrest.serialization.Model):
    """List of policy definitions.

    :ivar value: An array of policy definitions.
    :vartype value: list[~azure.mgmt.resource.policy.v2016_12_01.models.PolicyDefinition]
    :ivar next_link: The URL to use for getting the next set of results.
    :vartype next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[PolicyDefinition]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        value: Optional[List["PolicyDefinition"]] = None,
        next_link: Optional[str] = None,
        **kwargs
    ):
        """
        :keyword value: An array of policy definitions.
        :paramtype value: list[~azure.mgmt.resource.policy.v2016_12_01.models.PolicyDefinition]
        :keyword next_link: The URL to use for getting the next set of results.
        :paramtype next_link: str
        """
        super(PolicyDefinitionListResult, self).__init__(**kwargs)
        self.value = value
        self.next_link = next_link
