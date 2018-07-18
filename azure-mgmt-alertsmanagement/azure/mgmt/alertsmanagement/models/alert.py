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

from .resource import Resource


class Alert(Resource):
    """An alert created in alert management service.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Azure resource Id
    :vartype id: str
    :ivar type: Azure resource type
    :vartype type: str
    :ivar name: Azure resource name
    :vartype name: str
    :ivar severity: Severity of alert Sev1 being highest and Sev3 being
     lowest. Possible values include: 'Sev0', 'Sev1', 'Sev2', 'Sev3', 'Sev4'
    :vartype severity: str or ~azure.mgmt.alertsmanagement.models.Severity
    :ivar signal_type: Log based alert or metric based alert. Possible values
     include: 'Metric', 'Log', 'Unknown'
    :vartype signal_type: str or
     ~azure.mgmt.alertsmanagement.models.SignalType
    :ivar alert_state: Alert object state. Possible values include: 'New',
     'Acknowledged', 'Closed'
    :vartype alert_state: str or
     ~azure.mgmt.alertsmanagement.models.AlertState
    :ivar monitor_condition: Condition of the rule at the monitor service.
     Possible values include: 'Fired', 'Resolved'
    :vartype monitor_condition: str or
     ~azure.mgmt.alertsmanagement.models.MonitorCondition
    :param target_resource: Target ARM resource, on which alert got created.
    :type target_resource: str
    :param target_resource_name: Target ARM resource name, on which alert got
     created.
    :type target_resource_name: str
    :param target_resource_group: Resource group of target ARM resource.
    :type target_resource_group: str
    :param target_resource_type: Resource type of target ARM resource
    :type target_resource_type: str
    :ivar monitor_service: Monitor service which is the source of the alert
     object. Possible values include: 'Platform', 'Application Insights', 'Log
     Analytics', 'Infrastructure Insights', 'ActivityLog Administrative',
     'ActivityLog Security', 'ActivityLog Recommendation', 'ActivityLog
     Policy', 'ActivityLog Autoscale', 'ServiceHealth', 'SmartDetector',
     'Zabbix', 'SCOM', 'Nagios'
    :vartype monitor_service: str or
     ~azure.mgmt.alertsmanagement.models.MonitorService
    :ivar source_created_id: Unique Id created by monitor service
    :vartype source_created_id: str
    :ivar smart_group_id: Unique Id of the smart group
    :vartype smart_group_id: str
    :ivar smart_grouping_reason: Reason for addition to a smart group
    :vartype smart_grouping_reason: str
    :ivar start_date_time: Creation time(ISO-8601 format).
    :vartype start_date_time: datetime
    :ivar last_modified_date_time: Last modification time(ISO-8601 format).
    :vartype last_modified_date_time: datetime
    :ivar last_modified_user_name: User who last modified the alert.
    :vartype last_modified_user_name: str
    :ivar payload: More details which are contextual to the monitor service.
    :vartype payload: object
    """

    _validation = {
        'id': {'readonly': True},
        'type': {'readonly': True},
        'name': {'readonly': True},
        'severity': {'readonly': True},
        'signal_type': {'readonly': True},
        'alert_state': {'readonly': True},
        'monitor_condition': {'readonly': True},
        'monitor_service': {'readonly': True},
        'source_created_id': {'readonly': True},
        'smart_group_id': {'readonly': True},
        'smart_grouping_reason': {'readonly': True},
        'start_date_time': {'readonly': True},
        'last_modified_date_time': {'readonly': True},
        'last_modified_user_name': {'readonly': True},
        'payload': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'severity': {'key': 'properties.severity', 'type': 'str'},
        'signal_type': {'key': 'properties.signalType', 'type': 'str'},
        'alert_state': {'key': 'properties.alertState', 'type': 'str'},
        'monitor_condition': {'key': 'properties.monitorCondition', 'type': 'str'},
        'target_resource': {'key': 'properties.targetResource', 'type': 'str'},
        'target_resource_name': {'key': 'properties.targetResourceName', 'type': 'str'},
        'target_resource_group': {'key': 'properties.targetResourceGroup', 'type': 'str'},
        'target_resource_type': {'key': 'properties.targetResourceType', 'type': 'str'},
        'monitor_service': {'key': 'properties.monitorService', 'type': 'str'},
        'source_created_id': {'key': 'properties.sourceCreatedId', 'type': 'str'},
        'smart_group_id': {'key': 'properties.smartGroupId', 'type': 'str'},
        'smart_grouping_reason': {'key': 'properties.smartGroupingReason', 'type': 'str'},
        'start_date_time': {'key': 'properties.startDateTime', 'type': 'iso-8601'},
        'last_modified_date_time': {'key': 'properties.lastModifiedDateTime', 'type': 'iso-8601'},
        'last_modified_user_name': {'key': 'properties.lastModifiedUserName', 'type': 'str'},
        'payload': {'key': 'properties.payload', 'type': 'object'},
    }

    def __init__(self, **kwargs):
        super(Alert, self).__init__(**kwargs)
        self.severity = None
        self.signal_type = None
        self.alert_state = None
        self.monitor_condition = None
        self.target_resource = kwargs.get('target_resource', None)
        self.target_resource_name = kwargs.get('target_resource_name', None)
        self.target_resource_group = kwargs.get('target_resource_group', None)
        self.target_resource_type = kwargs.get('target_resource_type', None)
        self.monitor_service = None
        self.source_created_id = None
        self.smart_group_id = None
        self.smart_grouping_reason = None
        self.start_date_time = None
        self.last_modified_date_time = None
        self.last_modified_user_name = None
        self.payload = None