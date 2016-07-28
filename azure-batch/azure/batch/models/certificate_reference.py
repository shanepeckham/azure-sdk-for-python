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


class CertificateReference(Model):
    """A reference to a certificate to be installed on compute nodes in a pool.

    :param thumbprint: The thumbprint of the certificate.
    :type thumbprint: str
    :param thumbprint_algorithm: The algorithm with which the thumbprint is
     associated. This must be sha1.
    :type thumbprint_algorithm: str
    :param store_location: The location of the certificate store on the
     compute node into which to install the certificate. The default value is
     CurrentUser. Possible values include: 'currentuser', 'localmachine',
     'unmapped'
    :type store_location: str or :class:`CertificateStoreLocation
     <azure.batch.models.CertificateStoreLocation>`
    :param store_name: The name of the certificate store on the compute node
     into which to install the certificate. The default value is My.
    :type store_name: str
    :param visibility: Which user accounts on the compute node should have
     access to the private data of the certificate. This may be any subset of
     the values 'starttask', 'task' and 'remoteuser', separated by commas.
     The default is all accounts, corresponding to the string
     'starttask,task,remoteuser'.
    :type visibility: list of str or :class:`CertificateVisibility
     <azure.batch.models.CertificateVisibility>`
    """ 

    _validation = {
        'thumbprint': {'required': True},
        'thumbprint_algorithm': {'required': True},
    }

    _attribute_map = {
        'thumbprint': {'key': 'thumbprint', 'type': 'str'},
        'thumbprint_algorithm': {'key': 'thumbprintAlgorithm', 'type': 'str'},
        'store_location': {'key': 'storeLocation', 'type': 'CertificateStoreLocation'},
        'store_name': {'key': 'storeName', 'type': 'str'},
        'visibility': {'key': 'visibility', 'type': '[CertificateVisibility]'},
    }

    def __init__(self, thumbprint, thumbprint_algorithm, store_location=None, store_name=None, visibility=None):
        self.thumbprint = thumbprint
        self.thumbprint_algorithm = thumbprint_algorithm
        self.store_location = store_location
        self.store_name = store_name
        self.visibility = visibility