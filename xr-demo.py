"""
AUTHOR: IPvZero
DATE: 15th January 2021

WARNING: This script is designed to work on the Cisco IOS-XR Always-On Sandbox.
Be aware this Sandbox is a shared resource and if others are using it at the same time
you may experience failures/timeouts.

INSTRUCTIONS: This script utilised the Nornir Automation Framework and the Scrapli Netconf library.
You can install with either pip or pip3.
PIP:   python3 -m pip install nornir-scrapli
       python3 -m pip install nornir-jinja2 

PIP3: pip3 install nornir-scrapli
      pip3 install nornir-jinja2 
"""

from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_utils.plugins.tasks.data import load_yaml
from nornir_jinja2.plugins.tasks import template_file
from nornir_scrapli.tasks import (
    netconf_edit_config,
    netconf_commit,
    netconf_lock,
    netconf_unlock,
)

nr = InitNornir(config_file="config.yaml")


def load_vars(task):
    """
    Load host variables and bind them to a per-host dict key called "facts"
    """

    data = task.run(
        task=load_yaml,
        name="Loading Vars Into Memory...",
        file=f"./host_vars/{task.host}.yaml",
    )
    task.host["facts"] = data.result


def lock_config(task):
    task.run(task=netconf_lock, target="candidate", name="Locking...")


def config_bgp(task):
    """
    Build BGP config based on IOS-XR YANG Model
    Push configuration over NETCONF
    """

    bgp_template = task.run(
        task=template_file,
        name="Buildling BGP Configuration",
        template="bgp.j2",
        path="./templates",
    )
    bgp_output = bgp_template.result
    task.run(
        task=netconf_edit_config,
        name="Automating BGP",
        target="candidate",
        config=bgp_output,
    )


def config_ospf(task):
    """
    Build OSPF config based on IOS-XR YANG Model
    Push configuration over NETCONF
    """

    ospf_template = task.run(
        task=template_file,
        name="Buildling OSPF Configuration",
        template="ospf.j2",
        path="./templates",
    )
    ospf_output = ospf_template.result
    task.run(
        task=netconf_edit_config,
        name="Automating OSPF",
        target="candidate",
        config=ospf_output,
    )


def config_ntp(task):
    """
    Build NTP config based on IOS-XR YANG Model
    Push configuration over NETCONF
    """

    ntp_template = task.run(
        task=template_file,
        name="Buildling NTP Configuration",
        template="ntp.j2",
        path="./templates",
    )
    ntp_output = ntp_template.result
    task.run(
        task=netconf_edit_config,
        name="Automating NTP",
        target="candidate",
        config=ntp_output,
    )


def config_acl(task):
    """
    Build ACL config based on IOS-XR YANG Model
    Push configuration over NETCONF
    """

    acl_template = task.run(
        task=template_file,
        name="Buildling Configuration",
        template="acl.j2",
        path="./templates",
    )
    acl_output = acl_template.result
    task.run(
        task=netconf_edit_config,
        name="Automating ACL",
        target="candidate",
        config=acl_output,
    )


def commit_configs(task):
    """
    Commit the configuration changes.
    This moves then into the running config.
    """
    task.run(
        task=netconf_commit, name="Committing Changes into the Running Configuration"
    )


def unlock_config(task):
    task.run(task=netconf_unlock, target="candidate")


# DON'T COMMENT THIS ONE OUT - THIS LOADS THE VARIABLE DATA
var = nr.run(task=load_vars)
print_result(var)

# DON'T COMMENT THIS ONE OUT - THIS LOCKS THE CONFIGURATION DATASTORE
locker = nr.run(task=lock_config, name="NETCONF_LOCK")
print_result(locker)

# COMMENT THIS OUT IF YOU WANT TO SKIP BGP CONFIG
bgp_results = nr.run(task=config_bgp, name="BGP CONFIGURATION")
print_result(bgp_results)

# COMMENT THIS OUT IF YOU WANT TO SKIP OSPF CONFIG
ospf_results = nr.run(task=config_ospf, name="OSPF CONFIGURATION")
print_result(ospf_results)

# COMMENT THIS OUT IF YOU WANT TO SKIP NTP CONFIG
ntp_results = nr.run(task=config_ntp, name="NTP CONFIGURATION")
print_result(ntp_results)

# COMMENT THIS OUT IF YOU WANT TO SKIP ACL CONFIG
acl_results = nr.run(task=config_acl, name="ACL CONFIGUTATION")
print_result(acl_results)

# DON'T COMMENT THIS ONE OUT - THIS PUSHES THE CHANGES TO THE RUNNING CONFIG
commit_results = nr.run(task=commit_configs, name="NETCONF_COMMIT")
print_result(commit_results)

# DON'T COMMENT THIS OUT - THIS UNLOCKS THE CONFIGURATION DATASTORE
unlocker = nr.run(task=unlock_config, name="NETCONF_UNLOCK")
print_result(unlocker)
