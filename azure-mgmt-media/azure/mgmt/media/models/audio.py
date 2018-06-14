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

from .codec import Codec


class Audio(Codec):
    """Defines the common properties for all audio codecs.

    You probably want to use the sub-classes and not this class directly. Known
    sub-classes are: AacAudio

    All required parameters must be populated in order to send to Azure.

    :param label: An optional label for the codec. The label can be used to
     control muxing behavior.
    :type label: str
    :param odatatype: Required. Constant filled by server.
    :type odatatype: str
    :param channels: The number of channels in the audio.
    :type channels: int
    :param sampling_rate: The sampling rate to use for encoding in hertz.
    :type sampling_rate: int
    :param bitrate: The bitrate, in bits per second, of the output encoded
     audio.
    :type bitrate: int
    """

    _validation = {
        'odatatype': {'required': True},
    }

    _attribute_map = {
        'label': {'key': 'label', 'type': 'str'},
        'odatatype': {'key': '@odata\\.type', 'type': 'str'},
        'channels': {'key': 'channels', 'type': 'int'},
        'sampling_rate': {'key': 'samplingRate', 'type': 'int'},
        'bitrate': {'key': 'bitrate', 'type': 'int'},
    }

    _subtype_map = {
        'odatatype': {'#Microsoft.Media.AacAudio': 'AacAudio'}
    }

    def __init__(self, **kwargs):
        super(Audio, self).__init__(**kwargs)
        self.channels = kwargs.get('channels', None)
        self.sampling_rate = kwargs.get('sampling_rate', None)
        self.bitrate = kwargs.get('bitrate', None)
        self.odatatype = '#Microsoft.Media.Audio'