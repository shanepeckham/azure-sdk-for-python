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

from .resource_py3 import Resource


class RollingUpgradeStatusInfo(Resource):
    """The status of the latest virtual machine scale set rolling upgrade.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Resource Id
    :vartype id: str
    :ivar name: Resource name
    :vartype name: str
    :ivar type: Resource type
    :vartype type: str
    :param location: Required. Resource location
    :type location: str
    :param tags: Resource tags
    :type tags: dict[str, str]
    :ivar policy: The rolling upgrade policies applied for this upgrade.
    :vartype policy:
     ~azure.mgmt.compute.v2018_04_01.models.RollingUpgradePolicy
    :ivar running_status: Information about the current running state of the
     overall upgrade.
    :vartype running_status:
     ~azure.mgmt.compute.v2018_04_01.models.RollingUpgradeRunningStatus
    :ivar progress: Information about the number of virtual machine instances
     in each upgrade state.
    :vartype progress:
     ~azure.mgmt.compute.v2018_04_01.models.RollingUpgradeProgressInfo
    :ivar error: Error details for this upgrade, if there are any.
    :vartype error: ~azure.mgmt.compute.v2018_04_01.models.ApiError
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
        'policy': {'readonly': True},
        'running_status': {'readonly': True},
        'progress': {'readonly': True},
        'error': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'policy': {'key': 'properties.policy', 'type': 'RollingUpgradePolicy'},
        'running_status': {'key': 'properties.runningStatus', 'type': 'RollingUpgradeRunningStatus'},
        'progress': {'key': 'properties.progress', 'type': 'RollingUpgradeProgressInfo'},
        'error': {'key': 'properties.error', 'type': 'ApiError'},
    }

    def __init__(self, *, location: str, tags=None, **kwargs) -> None:
        super(RollingUpgradeStatusInfo, self).__init__(location=location, tags=tags, **kwargs)
        self.policy = None
        self.running_status = None
        self.progress = None
        self.error = None
