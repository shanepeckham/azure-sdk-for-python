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


class GalleryImageIdentifier(Model):
    """This is the gallery image identifier.

    :param publisher: The gallery image publisher name.
    :type publisher: str
    :param offer: The gallery image offer name.
    :type offer: str
    :param sku: The gallery image sku name.
    :type sku: str
    """

    _attribute_map = {
        'publisher': {'key': 'publisher', 'type': 'str'},
        'offer': {'key': 'offer', 'type': 'str'},
        'sku': {'key': 'sku', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(GalleryImageIdentifier, self).__init__(**kwargs)
        self.publisher = kwargs.get('publisher', None)
        self.offer = kwargs.get('offer', None)
        self.sku = kwargs.get('sku', None)
