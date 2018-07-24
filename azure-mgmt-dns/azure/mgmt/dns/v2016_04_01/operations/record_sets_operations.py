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

import uuid
from msrest.pipeline import ClientRawResponse
from msrestazure.azure_exceptions import CloudError

from .. import models


class RecordSetsOperations(object):
    """RecordSetsOperations operations.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    :ivar api_version: Specifies the API version. Constant value: "2016-04-01".
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):

        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self.api_version = "2016-04-01"

        self.config = config

    def update(
            self, resource_group_name, zone_name, relative_record_set_name, record_type, parameters, if_match=None, custom_headers=None, raw=False, **operation_config):
        """Updates a record set within a DNS zone.

        :param resource_group_name: The name of the resource group. The name
         is case insensitive.
        :type resource_group_name: str
        :param zone_name: The name of the DNS zone (without a terminating
         dot).
        :type zone_name: str
        :param relative_record_set_name: The name of the record set, relative
         to the name of the zone.
        :type relative_record_set_name: str
        :param record_type: The type of DNS record in this record set.
         Possible values include: 'A', 'AAAA', 'CNAME', 'MX', 'NS', 'PTR',
         'SOA', 'SRV', 'TXT'
        :type record_type: str or
         ~azure.mgmt.dns.v2016_04_01.models.RecordType
        :param parameters: Parameters supplied to the Update operation.
        :type parameters: ~azure.mgmt.dns.v2016_04_01.models.RecordSet
        :param if_match: The etag of the record set. Omit this value to always
         overwrite the current record set. Specify the last-seen etag value to
         prevent accidentally overwritting concurrent changes.
        :type if_match: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: RecordSet or ClientRawResponse if raw=true
        :rtype: ~azure.mgmt.dns.v2016_04_01.models.RecordSet or
         ~msrest.pipeline.ClientRawResponse
        :raises: :class:`CloudError<msrestazure.azure_exceptions.CloudError>`
        """
        # Construct URL
        url = self.update.metadata['url']
        path_format_arguments = {
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1, pattern=r'^[-\w\._\(\)]+$'),
            'zoneName': self._serialize.url("zone_name", zone_name, 'str'),
            'relativeRecordSetName': self._serialize.url("relative_record_set_name", relative_record_set_name, 'str', skip_quote=True),
            'recordType': self._serialize.url("record_type", record_type, 'RecordType'),
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if if_match is not None:
            header_parameters['If-Match'] = self._serialize.header("if_match", if_match, 'str')
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct body
        body_content = self._serialize.body(parameters, 'RecordSet')

        # Construct and send request
        request = self._client.patch(url, query_parameters, header_parameters, body_content)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            exp = CloudError(response)
            exp.request_id = response.headers.get('x-ms-request-id')
            raise exp

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('RecordSet', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    update.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/dnsZones/{zoneName}/{recordType}/{relativeRecordSetName}'}

    def create_or_update(
            self, resource_group_name, zone_name, relative_record_set_name, record_type, parameters, if_match=None, if_none_match=None, custom_headers=None, raw=False, **operation_config):
        """Creates or updates a record set within a DNS zone.

        :param resource_group_name: The name of the resource group. The name
         is case insensitive.
        :type resource_group_name: str
        :param zone_name: The name of the DNS zone (without a terminating
         dot).
        :type zone_name: str
        :param relative_record_set_name: The name of the record set, relative
         to the name of the zone.
        :type relative_record_set_name: str
        :param record_type: The type of DNS record in this record set. Record
         sets of type SOA can be updated but not created (they are created when
         the DNS zone is created). Possible values include: 'A', 'AAAA',
         'CNAME', 'MX', 'NS', 'PTR', 'SOA', 'SRV', 'TXT'
        :type record_type: str or
         ~azure.mgmt.dns.v2016_04_01.models.RecordType
        :param parameters: Parameters supplied to the CreateOrUpdate
         operation.
        :type parameters: ~azure.mgmt.dns.v2016_04_01.models.RecordSet
        :param if_match: The etag of the record set. Omit this value to always
         overwrite the current record set. Specify the last-seen etag value to
         prevent accidentally overwritting any concurrent changes.
        :type if_match: str
        :param if_none_match: Set to '*' to allow a new record set to be
         created, but to prevent updating an existing record set. Other values
         will be ignored.
        :type if_none_match: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: RecordSet or ClientRawResponse if raw=true
        :rtype: ~azure.mgmt.dns.v2016_04_01.models.RecordSet or
         ~msrest.pipeline.ClientRawResponse
        :raises: :class:`CloudError<msrestazure.azure_exceptions.CloudError>`
        """
        # Construct URL
        url = self.create_or_update.metadata['url']
        path_format_arguments = {
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1, pattern=r'^[-\w\._\(\)]+$'),
            'zoneName': self._serialize.url("zone_name", zone_name, 'str'),
            'relativeRecordSetName': self._serialize.url("relative_record_set_name", relative_record_set_name, 'str', skip_quote=True),
            'recordType': self._serialize.url("record_type", record_type, 'RecordType'),
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if if_match is not None:
            header_parameters['If-Match'] = self._serialize.header("if_match", if_match, 'str')
        if if_none_match is not None:
            header_parameters['If-None-Match'] = self._serialize.header("if_none_match", if_none_match, 'str')
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct body
        body_content = self._serialize.body(parameters, 'RecordSet')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200, 201]:
            exp = CloudError(response)
            exp.request_id = response.headers.get('x-ms-request-id')
            raise exp

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('RecordSet', response)
        if response.status_code == 201:
            deserialized = self._deserialize('RecordSet', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    create_or_update.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/dnsZones/{zoneName}/{recordType}/{relativeRecordSetName}'}

    def delete(
            self, resource_group_name, zone_name, relative_record_set_name, record_type, if_match=None, custom_headers=None, raw=False, **operation_config):
        """Deletes a record set from a DNS zone. This operation cannot be undone.

        :param resource_group_name: The name of the resource group. The name
         is case insensitive.
        :type resource_group_name: str
        :param zone_name: The name of the DNS zone (without a terminating
         dot).
        :type zone_name: str
        :param relative_record_set_name: The name of the record set, relative
         to the name of the zone.
        :type relative_record_set_name: str
        :param record_type: The type of DNS record in this record set. Record
         sets of type SOA cannot be deleted (they are deleted when the DNS zone
         is deleted). Possible values include: 'A', 'AAAA', 'CNAME', 'MX',
         'NS', 'PTR', 'SOA', 'SRV', 'TXT'
        :type record_type: str or
         ~azure.mgmt.dns.v2016_04_01.models.RecordType
        :param if_match: The etag of the record set. Omit this value to always
         delete the current record set. Specify the last-seen etag value to
         prevent accidentally deleting any concurrent changes.
        :type if_match: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises: :class:`CloudError<msrestazure.azure_exceptions.CloudError>`
        """
        # Construct URL
        url = self.delete.metadata['url']
        path_format_arguments = {
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1, pattern=r'^[-\w\._\(\)]+$'),
            'zoneName': self._serialize.url("zone_name", zone_name, 'str'),
            'relativeRecordSetName': self._serialize.url("relative_record_set_name", relative_record_set_name, 'str', skip_quote=True),
            'recordType': self._serialize.url("record_type", record_type, 'RecordType'),
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if if_match is not None:
            header_parameters['If-Match'] = self._serialize.header("if_match", if_match, 'str')
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct and send request
        request = self._client.delete(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200, 204]:
            exp = CloudError(response)
            exp.request_id = response.headers.get('x-ms-request-id')
            raise exp

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response
    delete.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/dnsZones/{zoneName}/{recordType}/{relativeRecordSetName}'}

    def get(
            self, resource_group_name, zone_name, relative_record_set_name, record_type, custom_headers=None, raw=False, **operation_config):
        """Gets a record set.

        :param resource_group_name: The name of the resource group. The name
         is case insensitive.
        :type resource_group_name: str
        :param zone_name: The name of the DNS zone (without a terminating
         dot).
        :type zone_name: str
        :param relative_record_set_name: The name of the record set, relative
         to the name of the zone.
        :type relative_record_set_name: str
        :param record_type: The type of DNS record in this record set.
         Possible values include: 'A', 'AAAA', 'CNAME', 'MX', 'NS', 'PTR',
         'SOA', 'SRV', 'TXT'
        :type record_type: str or
         ~azure.mgmt.dns.v2016_04_01.models.RecordType
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: RecordSet or ClientRawResponse if raw=true
        :rtype: ~azure.mgmt.dns.v2016_04_01.models.RecordSet or
         ~msrest.pipeline.ClientRawResponse
        :raises: :class:`CloudError<msrestazure.azure_exceptions.CloudError>`
        """
        # Construct URL
        url = self.get.metadata['url']
        path_format_arguments = {
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1, pattern=r'^[-\w\._\(\)]+$'),
            'zoneName': self._serialize.url("zone_name", zone_name, 'str'),
            'relativeRecordSetName': self._serialize.url("relative_record_set_name", relative_record_set_name, 'str', skip_quote=True),
            'recordType': self._serialize.url("record_type", record_type, 'RecordType'),
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            exp = CloudError(response)
            exp.request_id = response.headers.get('x-ms-request-id')
            raise exp

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('RecordSet', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/dnsZones/{zoneName}/{recordType}/{relativeRecordSetName}'}

    def list_by_type(
            self, resource_group_name, zone_name, record_type, top=None, recordsetnamesuffix=None, custom_headers=None, raw=False, **operation_config):
        """Lists the record sets of a specified type in a DNS zone.

        :param resource_group_name: The name of the resource group. The name
         is case insensitive.
        :type resource_group_name: str
        :param zone_name: The name of the DNS zone (without a terminating
         dot).
        :type zone_name: str
        :param record_type: The type of record sets to enumerate. Possible
         values include: 'A', 'AAAA', 'CNAME', 'MX', 'NS', 'PTR', 'SOA', 'SRV',
         'TXT'
        :type record_type: str or
         ~azure.mgmt.dns.v2016_04_01.models.RecordType
        :param top: The maximum number of record sets to return. If not
         specified, returns up to 100 record sets.
        :type top: int
        :param recordsetnamesuffix: The suffix label of the record set name
         that has to be used to filter the record set enumerations. If this
         parameter is specified, Enumeration will return only records that end
         with .<recordSetNameSuffix>
        :type recordsetnamesuffix: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: An iterator like instance of RecordSet
        :rtype:
         ~azure.mgmt.dns.v2016_04_01.models.RecordSetPaged[~azure.mgmt.dns.v2016_04_01.models.RecordSet]
        :raises: :class:`CloudError<msrestazure.azure_exceptions.CloudError>`
        """
        def internal_paging(next_link=None, raw=False):

            if not next_link:
                # Construct URL
                url = self.list_by_type.metadata['url']
                path_format_arguments = {
                    'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1, pattern=r'^[-\w\._\(\)]+$'),
                    'zoneName': self._serialize.url("zone_name", zone_name, 'str'),
                    'recordType': self._serialize.url("record_type", record_type, 'RecordType'),
                    'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str')
                }
                url = self._client.format_url(url, **path_format_arguments)

                # Construct parameters
                query_parameters = {}
                if top is not None:
                    query_parameters['$top'] = self._serialize.query("top", top, 'int')
                if recordsetnamesuffix is not None:
                    query_parameters['$recordsetnamesuffix'] = self._serialize.query("recordsetnamesuffix", recordsetnamesuffix, 'str')
                query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

            else:
                url = next_link
                query_parameters = {}

            # Construct headers
            header_parameters = {}
            header_parameters['Accept'] = 'application/json'
            if self.config.generate_client_request_id:
                header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
            if custom_headers:
                header_parameters.update(custom_headers)
            if self.config.accept_language is not None:
                header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

            # Construct and send request
            request = self._client.get(url, query_parameters, header_parameters)
            response = self._client.send(request, stream=False, **operation_config)

            if response.status_code not in [200]:
                exp = CloudError(response)
                exp.request_id = response.headers.get('x-ms-request-id')
                raise exp

            return response

        # Deserialize response
        deserialized = models.RecordSetPaged(internal_paging, self._deserialize.dependencies)

        if raw:
            header_dict = {}
            client_raw_response = models.RecordSetPaged(internal_paging, self._deserialize.dependencies, header_dict)
            return client_raw_response

        return deserialized
    list_by_type.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/dnsZones/{zoneName}/{recordType}'}

    def list_by_dns_zone(
            self, resource_group_name, zone_name, top=None, recordsetnamesuffix=None, custom_headers=None, raw=False, **operation_config):
        """Lists all record sets in a DNS zone.

        :param resource_group_name: The name of the resource group. The name
         is case insensitive.
        :type resource_group_name: str
        :param zone_name: The name of the DNS zone (without a terminating
         dot).
        :type zone_name: str
        :param top: The maximum number of record sets to return. If not
         specified, returns up to 100 record sets.
        :type top: int
        :param recordsetnamesuffix: The suffix label of the record set name
         that has to be used to filter the record set enumerations. If this
         parameter is specified, Enumeration will return only records that end
         with .<recordSetNameSuffix>
        :type recordsetnamesuffix: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: An iterator like instance of RecordSet
        :rtype:
         ~azure.mgmt.dns.v2016_04_01.models.RecordSetPaged[~azure.mgmt.dns.v2016_04_01.models.RecordSet]
        :raises: :class:`CloudError<msrestazure.azure_exceptions.CloudError>`
        """
        def internal_paging(next_link=None, raw=False):

            if not next_link:
                # Construct URL
                url = self.list_by_dns_zone.metadata['url']
                path_format_arguments = {
                    'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1, pattern=r'^[-\w\._\(\)]+$'),
                    'zoneName': self._serialize.url("zone_name", zone_name, 'str'),
                    'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str')
                }
                url = self._client.format_url(url, **path_format_arguments)

                # Construct parameters
                query_parameters = {}
                if top is not None:
                    query_parameters['$top'] = self._serialize.query("top", top, 'int')
                if recordsetnamesuffix is not None:
                    query_parameters['$recordsetnamesuffix'] = self._serialize.query("recordsetnamesuffix", recordsetnamesuffix, 'str')
                query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

            else:
                url = next_link
                query_parameters = {}

            # Construct headers
            header_parameters = {}
            header_parameters['Accept'] = 'application/json'
            if self.config.generate_client_request_id:
                header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
            if custom_headers:
                header_parameters.update(custom_headers)
            if self.config.accept_language is not None:
                header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

            # Construct and send request
            request = self._client.get(url, query_parameters, header_parameters)
            response = self._client.send(request, stream=False, **operation_config)

            if response.status_code not in [200]:
                exp = CloudError(response)
                exp.request_id = response.headers.get('x-ms-request-id')
                raise exp

            return response

        # Deserialize response
        deserialized = models.RecordSetPaged(internal_paging, self._deserialize.dependencies)

        if raw:
            header_dict = {}
            client_raw_response = models.RecordSetPaged(internal_paging, self._deserialize.dependencies, header_dict)
            return client_raw_response

        return deserialized
    list_by_dns_zone.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/dnsZones/{zoneName}/recordsets'}
