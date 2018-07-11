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


class ProvisionedResourceProperties(Model):
    """Describes common properties of a provisioned resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar provisioning_state: State of the resource.
    :vartype provisioning_state: str
    """

    _validation = {
        'provisioning_state': {'readonly': True},
    }

    _attribute_map = {
        'provisioning_state': {'key': 'provisioningState', 'type': 'str'},
    }

    def __init__(self, **kwargs) -> None:
        super(ProvisionedResourceProperties, self).__init__(**kwargs)
        self.provisioning_state = None
