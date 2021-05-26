# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

import msrest.serialization


class SmsSendResult(msrest.serialization.Model):
    """Response for a single recipient.

    All required parameters must be populated in order to send to Azure.

    :param to: Required. The recipient's phone number in E.164 format.
    :type to: str
    :param message_id: The identifier of the outgoing Sms message. Only present if message
     processed.
    :type message_id: str
    :param http_status_code: Required. HTTP Status code.
    :type http_status_code: int
    :param successful: Required. Indicates if the message is processed successfully or not.
    :type successful: bool
    :param error_message: Optional error message in case of 4xx/5xx/repeatable errors.
    :type error_message: str
    """

    _validation = {
        'to': {'required': True},
        'http_status_code': {'required': True},
        'successful': {'required': True},
    }

    _attribute_map = {
        'to': {'key': 'to', 'type': 'str'},
        'message_id': {'key': 'messageId', 'type': 'str'},
        'http_status_code': {'key': 'httpStatusCode', 'type': 'int'},
        'successful': {'key': 'successful', 'type': 'bool'},
        'error_message': {'key': 'errorMessage', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(SmsSendResult, self).__init__(**kwargs)
        self.to = kwargs['to']
        self.message_id = kwargs.get('message_id', None)
        self.http_status_code = kwargs['http_status_code']
        self.successful = kwargs['successful']
        self.error_message = kwargs.get('error_message', None)