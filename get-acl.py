"""
AUTHOR: IPvZero
Date: 15 January 2021

This script retrieves ACL configuration information
"""

from nornir_scrapli.tasks import netconf_get_config
from nornir_utils.plugins.functions import print_result
from nornir import InitNornir

nr = InitNornir(config_file="config.yaml")

acl_filter = """
 <ipv4-acl-and-prefix-list xmlns="http://cisco.com/ns/yang/Cisco-IOS-XR-ipv4-acl-cfg">
</ipv4-acl-and-prefix-list>
"""


def get_yang(task):
    """ Pull ACL Configuration """
    task.run(
        task=netconf_get_config,
        source="running",
        filter_type="subtree",
        filters=acl_filter,
    )


result = nr.run(task=get_yang)
print_result(result)
