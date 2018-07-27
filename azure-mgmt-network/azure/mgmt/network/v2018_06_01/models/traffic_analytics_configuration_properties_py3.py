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


class TrafficAnalyticsConfigurationProperties(Model):
    """Parameters that define the configuration of traffic analytics.

    All required parameters must be populated in order to send to Azure.

    :param enabled: Required. Flag to enable/disable traffic analytics.
    :type enabled: bool
    :param workspace_id: Required. The resource guid of the attached workspace
    :type workspace_id: str
    :param workspace_region: Required. The location of the attached workspace
    :type workspace_region: str
    :param workspace_resource_id: Required. Resource Id of the attached
     workspace
    :type workspace_resource_id: str
    """

    _validation = {
        'enabled': {'required': True},
        'workspace_id': {'required': True},
        'workspace_region': {'required': True},
        'workspace_resource_id': {'required': True},
    }

    _attribute_map = {
        'enabled': {'key': 'enabled', 'type': 'bool'},
        'workspace_id': {'key': 'workspaceId', 'type': 'str'},
        'workspace_region': {'key': 'workspaceRegion', 'type': 'str'},
        'workspace_resource_id': {'key': 'workspaceResourceId', 'type': 'str'},
    }

    def __init__(self, *, enabled: bool, workspace_id: str, workspace_region: str, workspace_resource_id: str, **kwargs) -> None:
        super(TrafficAnalyticsConfigurationProperties, self).__init__(**kwargs)
        self.enabled = enabled
        self.workspace_id = workspace_id
        self.workspace_region = workspace_region
        self.workspace_resource_id = workspace_resource_id
