"""
AUTHOR: IPvZero
Date: 15 January 2021

This script retrieves BGP configuration information
"""

from nornir_scrapli.tasks import netconf_get_config
from nornir_utils.plugins.functions import print_result
from nornir import InitNornir

nr = InitNornir(config_file="config.yaml")

bgp_filter = """
<bgp xmlns="http://cisco.com/ns/yang/Cisco-IOS-XR-ipv4-bgp-cfg">
</bgp> """


def get_yang(task):
    """ Pull BGP Configuration """
    task.run(
        task=netconf_get_config,
        source="running",
        filter_type="subtree",
        filters=bgp_filter,
    )


result = nr.run(task=get_yang)
print_result(result)
