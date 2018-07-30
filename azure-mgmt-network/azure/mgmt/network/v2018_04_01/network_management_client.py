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

from msrest.service_client import SDKClient
from msrest import Serializer, Deserializer
from msrestazure import AzureConfiguration
from .version import VERSION
from msrest.pipeline import ClientRawResponse
from msrestazure.azure_exceptions import CloudError
from msrest.polling import LROPoller, NoPolling
from msrestazure.polling.arm_polling import ARMPolling
import uuid
from .operations.azure_firewalls_operations import AzureFirewallsOperations
from .operations.application_gateways_operations import ApplicationGatewaysOperations
from .operations.application_security_groups_operations import ApplicationSecurityGroupsOperations
from .operations.ddos_protection_plans_operations import DdosProtectionPlansOperations
from .operations.available_endpoint_services_operations import AvailableEndpointServicesOperations
from .operations.express_route_circuit_authorizations_operations import ExpressRouteCircuitAuthorizationsOperations
from .operations.express_route_circuit_peerings_operations import ExpressRouteCircuitPeeringsOperations
from .operations.express_route_circuit_connections_operations import ExpressRouteCircuitConnectionsOperations
from .operations.express_route_circuits_operations import ExpressRouteCircuitsOperations
from .operations.express_route_service_providers_operations import ExpressRouteServiceProvidersOperations
from .operations.express_route_cross_connections_operations import ExpressRouteCrossConnectionsOperations
from .operations.express_route_cross_connection_peerings_operations import ExpressRouteCrossConnectionPeeringsOperations
from .operations.load_balancers_operations import LoadBalancersOperations
from .operations.load_balancer_backend_address_pools_operations import LoadBalancerBackendAddressPoolsOperations
from .operations.load_balancer_frontend_ip_configurations_operations import LoadBalancerFrontendIPConfigurationsOperations
from .operations.inbound_nat_rules_operations import InboundNatRulesOperations
from .operations.load_balancer_load_balancing_rules_operations import LoadBalancerLoadBalancingRulesOperations
from .operations.load_balancer_network_interfaces_operations import LoadBalancerNetworkInterfacesOperations
from .operations.load_balancer_probes_operations import LoadBalancerProbesOperations
from .operations.network_interfaces_operations import NetworkInterfacesOperations
from .operations.network_interface_ip_configurations_operations import NetworkInterfaceIPConfigurationsOperations
from .operations.network_interface_load_balancers_operations import NetworkInterfaceLoadBalancersOperations
from .operations.network_security_groups_operations import NetworkSecurityGroupsOperations
from .operations.security_rules_operations import SecurityRulesOperations
from .operations.default_security_rules_operations import DefaultSecurityRulesOperations
from .operations.network_watchers_operations import NetworkWatchersOperations
from .operations.packet_captures_operations import PacketCapturesOperations
from .operations.connection_monitors_operations import ConnectionMonitorsOperations
from .operations.operations import Operations
from .operations.public_ip_addresses_operations import PublicIPAddressesOperations
from .operations.route_filters_operations import RouteFiltersOperations
from .operations.route_filter_rules_operations import RouteFilterRulesOperations
from .operations.route_tables_operations import RouteTablesOperations
from .operations.routes_operations import RoutesOperations
from .operations.bgp_service_communities_operations import BgpServiceCommunitiesOperations
from .operations.usages_operations import UsagesOperations
from .operations.virtual_networks_operations import VirtualNetworksOperations
from .operations.subnets_operations import SubnetsOperations
from .operations.virtual_network_peerings_operations import VirtualNetworkPeeringsOperations
from .operations.virtual_network_gateways_operations import VirtualNetworkGatewaysOperations
from .operations.virtual_network_gateway_connections_operations import VirtualNetworkGatewayConnectionsOperations
from .operations.local_network_gateways_operations import LocalNetworkGatewaysOperations
from .operations.virtual_wa_ns_operations import VirtualWANsOperations
from .operations.vpn_sites_operations import VpnSitesOperations
from .operations.vpn_sites_configuration_operations import VpnSitesConfigurationOperations
from .operations.virtual_hubs_operations import VirtualHubsOperations
from .operations.hub_virtual_network_connections_operations import HubVirtualNetworkConnectionsOperations
from .operations.vpn_gateways_operations import VpnGatewaysOperations
from .operations.vpn_connections_operations import VpnConnectionsOperations
from . import models


class NetworkManagementClientConfiguration(AzureConfiguration):
    """Configuration for NetworkManagementClient
    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: The subscription credentials which uniquely
     identify the Microsoft Azure subscription. The subscription ID forms part
     of the URI for every service call.
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, subscription_id, base_url=None):

        if credentials is None:
            raise ValueError("Parameter 'credentials' must not be None.")
        if subscription_id is None:
            raise ValueError("Parameter 'subscription_id' must not be None.")
        if not base_url:
            base_url = 'https://management.azure.com'

        super(NetworkManagementClientConfiguration, self).__init__(base_url)

        self.add_user_agent('azure-mgmt-network/{}'.format(VERSION))
        self.add_user_agent('Azure-SDK-For-Python')

        self.credentials = credentials
        self.subscription_id = subscription_id


class NetworkManagementClient(SDKClient):
    """Network Client

    :ivar config: Configuration for client.
    :vartype config: NetworkManagementClientConfiguration

    :ivar azure_firewalls: AzureFirewalls operations
    :vartype azure_firewalls: azure.mgmt.network.v2018_04_01.operations.AzureFirewallsOperations
    :ivar application_gateways: ApplicationGateways operations
    :vartype application_gateways: azure.mgmt.network.v2018_04_01.operations.ApplicationGatewaysOperations
    :ivar application_security_groups: ApplicationSecurityGroups operations
    :vartype application_security_groups: azure.mgmt.network.v2018_04_01.operations.ApplicationSecurityGroupsOperations
    :ivar ddos_protection_plans: DdosProtectionPlans operations
    :vartype ddos_protection_plans: azure.mgmt.network.v2018_04_01.operations.DdosProtectionPlansOperations
    :ivar available_endpoint_services: AvailableEndpointServices operations
    :vartype available_endpoint_services: azure.mgmt.network.v2018_04_01.operations.AvailableEndpointServicesOperations
    :ivar express_route_circuit_authorizations: ExpressRouteCircuitAuthorizations operations
    :vartype express_route_circuit_authorizations: azure.mgmt.network.v2018_04_01.operations.ExpressRouteCircuitAuthorizationsOperations
    :ivar express_route_circuit_peerings: ExpressRouteCircuitPeerings operations
    :vartype express_route_circuit_peerings: azure.mgmt.network.v2018_04_01.operations.ExpressRouteCircuitPeeringsOperations
    :ivar express_route_circuit_connections: ExpressRouteCircuitConnections operations
    :vartype express_route_circuit_connections: azure.mgmt.network.v2018_04_01.operations.ExpressRouteCircuitConnectionsOperations
    :ivar express_route_circuits: ExpressRouteCircuits operations
    :vartype express_route_circuits: azure.mgmt.network.v2018_04_01.operations.ExpressRouteCircuitsOperations
    :ivar express_route_service_providers: ExpressRouteServiceProviders operations
    :vartype express_route_service_providers: azure.mgmt.network.v2018_04_01.operations.ExpressRouteServiceProvidersOperations
    :ivar express_route_cross_connections: ExpressRouteCrossConnections operations
    :vartype express_route_cross_connections: azure.mgmt.network.v2018_04_01.operations.ExpressRouteCrossConnectionsOperations
    :ivar express_route_cross_connection_peerings: ExpressRouteCrossConnectionPeerings operations
    :vartype express_route_cross_connection_peerings: azure.mgmt.network.v2018_04_01.operations.ExpressRouteCrossConnectionPeeringsOperations
    :ivar load_balancers: LoadBalancers operations
    :vartype load_balancers: azure.mgmt.network.v2018_04_01.operations.LoadBalancersOperations
    :ivar load_balancer_backend_address_pools: LoadBalancerBackendAddressPools operations
    :vartype load_balancer_backend_address_pools: azure.mgmt.network.v2018_04_01.operations.LoadBalancerBackendAddressPoolsOperations
    :ivar load_balancer_frontend_ip_configurations: LoadBalancerFrontendIPConfigurations operations
    :vartype load_balancer_frontend_ip_configurations: azure.mgmt.network.v2018_04_01.operations.LoadBalancerFrontendIPConfigurationsOperations
    :ivar inbound_nat_rules: InboundNatRules operations
    :vartype inbound_nat_rules: azure.mgmt.network.v2018_04_01.operations.InboundNatRulesOperations
    :ivar load_balancer_load_balancing_rules: LoadBalancerLoadBalancingRules operations
    :vartype load_balancer_load_balancing_rules: azure.mgmt.network.v2018_04_01.operations.LoadBalancerLoadBalancingRulesOperations
    :ivar load_balancer_network_interfaces: LoadBalancerNetworkInterfaces operations
    :vartype load_balancer_network_interfaces: azure.mgmt.network.v2018_04_01.operations.LoadBalancerNetworkInterfacesOperations
    :ivar load_balancer_probes: LoadBalancerProbes operations
    :vartype load_balancer_probes: azure.mgmt.network.v2018_04_01.operations.LoadBalancerProbesOperations
    :ivar network_interfaces: NetworkInterfaces operations
    :vartype network_interfaces: azure.mgmt.network.v2018_04_01.operations.NetworkInterfacesOperations
    :ivar network_interface_ip_configurations: NetworkInterfaceIPConfigurations operations
    :vartype network_interface_ip_configurations: azure.mgmt.network.v2018_04_01.operations.NetworkInterfaceIPConfigurationsOperations
    :ivar network_interface_load_balancers: NetworkInterfaceLoadBalancers operations
    :vartype network_interface_load_balancers: azure.mgmt.network.v2018_04_01.operations.NetworkInterfaceLoadBalancersOperations
    :ivar network_security_groups: NetworkSecurityGroups operations
    :vartype network_security_groups: azure.mgmt.network.v2018_04_01.operations.NetworkSecurityGroupsOperations
    :ivar security_rules: SecurityRules operations
    :vartype security_rules: azure.mgmt.network.v2018_04_01.operations.SecurityRulesOperations
    :ivar default_security_rules: DefaultSecurityRules operations
    :vartype default_security_rules: azure.mgmt.network.v2018_04_01.operations.DefaultSecurityRulesOperations
    :ivar network_watchers: NetworkWatchers operations
    :vartype network_watchers: azure.mgmt.network.v2018_04_01.operations.NetworkWatchersOperations
    :ivar packet_captures: PacketCaptures operations
    :vartype packet_captures: azure.mgmt.network.v2018_04_01.operations.PacketCapturesOperations
    :ivar connection_monitors: ConnectionMonitors operations
    :vartype connection_monitors: azure.mgmt.network.v2018_04_01.operations.ConnectionMonitorsOperations
    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.network.v2018_04_01.operations.Operations
    :ivar public_ip_addresses: PublicIPAddresses operations
    :vartype public_ip_addresses: azure.mgmt.network.v2018_04_01.operations.PublicIPAddressesOperations
    :ivar route_filters: RouteFilters operations
    :vartype route_filters: azure.mgmt.network.v2018_04_01.operations.RouteFiltersOperations
    :ivar route_filter_rules: RouteFilterRules operations
    :vartype route_filter_rules: azure.mgmt.network.v2018_04_01.operations.RouteFilterRulesOperations
    :ivar route_tables: RouteTables operations
    :vartype route_tables: azure.mgmt.network.v2018_04_01.operations.RouteTablesOperations
    :ivar routes: Routes operations
    :vartype routes: azure.mgmt.network.v2018_04_01.operations.RoutesOperations
    :ivar bgp_service_communities: BgpServiceCommunities operations
    :vartype bgp_service_communities: azure.mgmt.network.v2018_04_01.operations.BgpServiceCommunitiesOperations
    :ivar usages: Usages operations
    :vartype usages: azure.mgmt.network.v2018_04_01.operations.UsagesOperations
    :ivar virtual_networks: VirtualNetworks operations
    :vartype virtual_networks: azure.mgmt.network.v2018_04_01.operations.VirtualNetworksOperations
    :ivar subnets: Subnets operations
    :vartype subnets: azure.mgmt.network.v2018_04_01.operations.SubnetsOperations
    :ivar virtual_network_peerings: VirtualNetworkPeerings operations
    :vartype virtual_network_peerings: azure.mgmt.network.v2018_04_01.operations.VirtualNetworkPeeringsOperations
    :ivar virtual_network_gateways: VirtualNetworkGateways operations
    :vartype virtual_network_gateways: azure.mgmt.network.v2018_04_01.operations.VirtualNetworkGatewaysOperations
    :ivar virtual_network_gateway_connections: VirtualNetworkGatewayConnections operations
    :vartype virtual_network_gateway_connections: azure.mgmt.network.v2018_04_01.operations.VirtualNetworkGatewayConnectionsOperations
    :ivar local_network_gateways: LocalNetworkGateways operations
    :vartype local_network_gateways: azure.mgmt.network.v2018_04_01.operations.LocalNetworkGatewaysOperations
    :ivar virtual_wa_ns: VirtualWANs operations
    :vartype virtual_wa_ns: azure.mgmt.network.v2018_04_01.operations.VirtualWANsOperations
    :ivar vpn_sites: VpnSites operations
    :vartype vpn_sites: azure.mgmt.network.v2018_04_01.operations.VpnSitesOperations
    :ivar vpn_sites_configuration: VpnSitesConfiguration operations
    :vartype vpn_sites_configuration: azure.mgmt.network.v2018_04_01.operations.VpnSitesConfigurationOperations
    :ivar virtual_hubs: VirtualHubs operations
    :vartype virtual_hubs: azure.mgmt.network.v2018_04_01.operations.VirtualHubsOperations
    :ivar hub_virtual_network_connections: HubVirtualNetworkConnections operations
    :vartype hub_virtual_network_connections: azure.mgmt.network.v2018_04_01.operations.HubVirtualNetworkConnectionsOperations
    :ivar vpn_gateways: VpnGateways operations
    :vartype vpn_gateways: azure.mgmt.network.v2018_04_01.operations.VpnGatewaysOperations
    :ivar vpn_connections: VpnConnections operations
    :vartype vpn_connections: azure.mgmt.network.v2018_04_01.operations.VpnConnectionsOperations

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: The subscription credentials which uniquely
     identify the Microsoft Azure subscription. The subscription ID forms part
     of the URI for every service call.
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, subscription_id, base_url=None):

        self.config = NetworkManagementClientConfiguration(credentials, subscription_id, base_url)
        super(NetworkManagementClient, self).__init__(self.config.credentials, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.azure_firewalls = AzureFirewallsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.application_gateways = ApplicationGatewaysOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.application_security_groups = ApplicationSecurityGroupsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.ddos_protection_plans = DdosProtectionPlansOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.available_endpoint_services = AvailableEndpointServicesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.express_route_circuit_authorizations = ExpressRouteCircuitAuthorizationsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.express_route_circuit_peerings = ExpressRouteCircuitPeeringsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.express_route_circuit_connections = ExpressRouteCircuitConnectionsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.express_route_circuits = ExpressRouteCircuitsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.express_route_service_providers = ExpressRouteServiceProvidersOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.express_route_cross_connections = ExpressRouteCrossConnectionsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.express_route_cross_connection_peerings = ExpressRouteCrossConnectionPeeringsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.load_balancers = LoadBalancersOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.load_balancer_backend_address_pools = LoadBalancerBackendAddressPoolsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.load_balancer_frontend_ip_configurations = LoadBalancerFrontendIPConfigurationsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.inbound_nat_rules = InboundNatRulesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.load_balancer_load_balancing_rules = LoadBalancerLoadBalancingRulesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.load_balancer_network_interfaces = LoadBalancerNetworkInterfacesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.load_balancer_probes = LoadBalancerProbesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.network_interfaces = NetworkInterfacesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.network_interface_ip_configurations = NetworkInterfaceIPConfigurationsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.network_interface_load_balancers = NetworkInterfaceLoadBalancersOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.network_security_groups = NetworkSecurityGroupsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.security_rules = SecurityRulesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.default_security_rules = DefaultSecurityRulesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.network_watchers = NetworkWatchersOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.packet_captures = PacketCapturesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.connection_monitors = ConnectionMonitorsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.operations = Operations(
            self._client, self.config, self._serialize, self._deserialize)
        self.public_ip_addresses = PublicIPAddressesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.route_filters = RouteFiltersOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.route_filter_rules = RouteFilterRulesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.route_tables = RouteTablesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.routes = RoutesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.bgp_service_communities = BgpServiceCommunitiesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.usages = UsagesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.virtual_networks = VirtualNetworksOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.subnets = SubnetsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.virtual_network_peerings = VirtualNetworkPeeringsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.virtual_network_gateways = VirtualNetworkGatewaysOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.virtual_network_gateway_connections = VirtualNetworkGatewayConnectionsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.local_network_gateways = LocalNetworkGatewaysOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.virtual_wa_ns = VirtualWANsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.vpn_sites = VpnSitesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.vpn_sites_configuration = VpnSitesConfigurationOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.virtual_hubs = VirtualHubsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.hub_virtual_network_connections = HubVirtualNetworkConnectionsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.vpn_gateways = VpnGatewaysOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.vpn_connections = VpnConnectionsOperations(
            self._client, self.config, self._serialize, self._deserialize)

    def check_dns_name_availability(
            self, location, domain_name_label, custom_headers=None, raw=False, **operation_config):
        """Checks whether a domain name in the cloudapp.azure.com zone is
        available for use.

        :param location: The location of the domain name.
        :type location: str
        :param domain_name_label: The domain name to be verified. It must
         conform to the following regular expression:
         ^[a-z][a-z0-9-]{1,61}[a-z0-9]$.
        :type domain_name_label: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: DnsNameAvailabilityResult or ClientRawResponse if raw=true
        :rtype:
         ~azure.mgmt.network.v2018_04_01.models.DnsNameAvailabilityResult or
         ~msrest.pipeline.ClientRawResponse
        :raises: :class:`CloudError<msrestazure.azure_exceptions.CloudError>`
        """
        api_version = "2018-04-01"

        # Construct URL
        url = self.check_dns_name_availability.metadata['url']
        path_format_arguments = {
            'location': self._serialize.url("location", location, 'str'),
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['domainNameLabel'] = self._serialize.query("domain_name_label", domain_name_label, 'str')
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

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
            deserialized = self._deserialize('DnsNameAvailabilityResult', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    check_dns_name_availability.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.Network/locations/{location}/CheckDnsNameAvailability'}
