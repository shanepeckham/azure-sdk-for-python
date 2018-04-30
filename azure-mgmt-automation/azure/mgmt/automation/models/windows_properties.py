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


class WindowsProperties(Model):
    """Windows specific update configuration.

    :param included_update_classifications: Update classification included in
     the software update configuration. A comma separated string with required
     values. Possible values include: 'Unclassified', 'Critical', 'Security',
     'UpdateRollup', 'FeaturePack', 'ServicePack', 'Definition', 'Tools',
     'Updates'
    :type included_update_classifications: str or
     ~azure.mgmt.automation.models.WindowsUpdateClasses
    :param excluded_kb_numbers: KB numbers excluded from the software update
     configuration.
    :type excluded_kb_numbers: list[str]
    :param included_kb_numbers: KB numbers included from the software update
     configuration.
    :type included_kb_numbers: list[str]
    :param reboot_setting: Reboot setting for the software update
     configuration.
    :type reboot_setting: str
    """

    _attribute_map = {
        'included_update_classifications': {'key': 'includedUpdateClassifications', 'type': 'str'},
        'excluded_kb_numbers': {'key': 'excludedKbNumbers', 'type': '[str]'},
        'included_kb_numbers': {'key': 'includedKbNumbers', 'type': '[str]'},
        'reboot_setting': {'key': 'rebootSetting', 'type': 'str'},
    }

    def __init__(self, included_update_classifications=None, excluded_kb_numbers=None, included_kb_numbers=None, reboot_setting=None):
        super(WindowsProperties, self).__init__()
        self.included_update_classifications = included_update_classifications
        self.excluded_kb_numbers = excluded_kb_numbers
        self.included_kb_numbers = included_kb_numbers
        self.reboot_setting = reboot_setting
