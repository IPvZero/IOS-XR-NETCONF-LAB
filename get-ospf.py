"""
AUTHOR: IPvZero
Date: 15 January 2021

This script retrieves OSPF configuration information
"""

from nornir_scrapli.tasks import netconf_get_config
from nornir_utils.plugins.functions import print_result
from nornir import InitNornir

nr = InitNornir(config_file="config.yaml")

ospf_filter = """
<ospf xmlns="http://cisco.com/ns/yang/Cisco-IOS-XR-ipv4-ospf-cfg">
</ospf>"""


def get_yang(task):
    """ Pull OSPF Configuration """
    task.run(
        task=netconf_get_config,
        source="running",
        filter_type="subtree",
        filters=ospf_filter,
    )


result = nr.run(task=get_yang)
print_result(result)
