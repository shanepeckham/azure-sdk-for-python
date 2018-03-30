# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ContainerExecResponse(Model):
    """The information for the container exec command.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar web_socket_uri: The uri for the exec websocket.
    :vartype web_socket_uri: str
    :ivar password: The password to start the exec command.
    :vartype password: str
    """

    _validation = {
        'web_socket_uri': {'readonly': True},
        'password': {'readonly': True},
    }

    _attribute_map = {
        'web_socket_uri': {'key': 'webSocketUri', 'type': 'str'},
        'password': {'key': 'password', 'type': 'str'},
    }

    def __init__(self, **kwargs) -> None:
        super(ContainerExecResponse, self).__init__(**kwargs)
        self.web_socket_uri = None
        self.password = None