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


class VerifyFaceToFaceRequest(Model):
    """Request body for verify operation.

    All required parameters must be populated in order to send to Azure.

    :param face_id1: Required. FaceId of the first face, comes from Face -
     Detect
    :type face_id1: str
    :param face_id2: Required. FaceId of the second face, comes from Face -
     Detect
    :type face_id2: str
    """

    _validation = {
        'face_id1': {'required': True},
        'face_id2': {'required': True},
    }

    _attribute_map = {
        'face_id1': {'key': 'faceId1', 'type': 'str'},
        'face_id2': {'key': 'faceId2', 'type': 'str'},
    }

    def __init__(self, *, face_id1: str, face_id2: str, **kwargs) -> None:
        super(VerifyFaceToFaceRequest, self).__init__(**kwargs)
        self.face_id1 = face_id1
        self.face_id2 = face_id2
