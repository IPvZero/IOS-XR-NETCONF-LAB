"""
AUTHOR: IPvZero
Date: 15 January 2021

This script retrieves NTP configuration information
"""

from nornir_scrapli.tasks import netconf_get_config
from nornir_utils.plugins.functions import print_result
from nornir import InitNornir

nr = InitNornir(config_file="config.yaml")

ntp_filter = """
<ntp xmlns="http://cisco.com/ns/yang/Cisco-IOS-XR-ip-ntp-cfg">
</ntp>"""


def get_yang(task):
    """ Pull NTP Configuration """
    task.run(
        task=netconf_get_config,
        source="running",
        filter_type="subtree",
        filters=ntp_filter,
    )


result = nr.run(task=get_yang)
print_result(result)
