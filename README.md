# IOS-XR NETCONF LAB
This lab uses NETCONF to configure the IOS-XR Always On Sandbox.
-------------------------------------------------------------------
## Dependencies

```
pip3 install nornir-scrapli
pip3 install nornir-jinja2 
```
----------------------------------------------------------------
### WARNING
This lab uses a shared resource. If others are using it at the same you may experience errors (lock denied...) and failures due to timeouts.
When this happens you will need to wait until the resource is freed up before trying again.

### LAB INSTRUCTIONS
Pip install the dependencies and git clone the repository. Change into the ```IOS-XR-NETCONF-LAB``` directory.

To change the configurations simply enter the ```host_vars``` directory and modify the values in the ```R1.yaml``` file.

#### To execute the script:
```python3 xr-demo.py```

-------------------------------------------------

#### To manually log into the XR Always-On Sandbox and run show commands for verification:
```ssh admin@sbx-iosxr-mgmt.cisco.com -p 8181```

Then enter the password: 
```C1sco12345```

-------------------------------------------------

#### You can also retrieve the configuration information directly over NETCONF using the scripts in this repo.

##### To retrieve Access Control List configuration information:
```python3 get-acl.py```

##### To retrieve BGP configurarion information:
```python3 get-bgp.py```

##### To retrieve OSPF configuration information:
```python3 get-ospf.py```

##### To retrieve NTP configuration information:
```python3 get-ntp.py```

-------------------------------------------------
## Video Walkthrough
You can find a video walkthrough of this lab on my [youtube](https://www.youtube.com/watch?v=tFN7-jXX2dQ) channel!


### About Me
My name's John McGovern, I maintain a Youtube channel called IPvZero and I am trainer for CBT Nuggets. 

I create instructional videos on Python Network Automation.

### Contact

[Twitter](https://twitter.com/IPvZero)

[Youtube](https://youtube.com/c/IPvZero)

[LinkedIn](https://www.linkedin.com/in/ipvzero)

### CBT Nuggets 

[Advanced Network Automation with Cisco and Python](http://learn.gg/adv-net)

