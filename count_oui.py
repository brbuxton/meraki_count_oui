"""
This is a simple example of counting all of the occurrences of a specific OUI across all of the networks in a
Meraki org.  The Meraki Python SDK looks for your API key in the environment variable MERAKI_DASHBOARD_API_KEY
"""
import meraki

oui = 'e0:55:3d'
oui_count = 0

dashboard = meraki.DashboardAPI()
orgs = dashboard.organizations.getOrganizations()
# print(orgs) # uncomment to see the orgs the API key has access to
for org in orgs:
    # print(org['id']) # uncomment to see each organization ID on a line
    try:
        networks = dashboard.organizations.getOrganizationNetworks(organizationId=org['id'])
        for network in networks:
            # print(network['id']) # uncomment to see each network ID for each org on it's own line
            try:
                clients = dashboard.networks.getNetworkClients(network['id'], total_pages='all')
                for client in clients:
                    # print(client['mac']) # uncomment to see the mac address of every client on each network on a line
                    if oui in client['mac']:
                        oui_count += 1
            except:
                pass
    except:
        pass
print(oui_count)
