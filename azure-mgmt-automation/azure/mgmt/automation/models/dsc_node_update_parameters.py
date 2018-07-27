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


class DscNodeUpdateParameters(Model):
    """The parameters supplied to the update dsc node operation.

    :param node_id: Gets or sets the id of the dsc node.
    :type node_id: str
    :param properties:
    :type properties:
     ~azure.mgmt.automation.models.DscNodeUpdateParametersProperties
    """

    _attribute_map = {
        'node_id': {'key': 'nodeId', 'type': 'str'},
        'properties': {'key': 'properties', 'type': 'DscNodeUpdateParametersProperties'},
    }

    def __init__(self, **kwargs):
        super(DscNodeUpdateParameters, self).__init__(**kwargs)
        self.node_id = kwargs.get('node_id', None)
        self.properties = kwargs.get('properties', None)
