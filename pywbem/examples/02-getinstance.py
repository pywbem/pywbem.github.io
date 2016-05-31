#!/usr/bin/env python
#
# Demonstrate calling GetInstance.
#
# Enumerate the instance paths of CIM_OperatingSystem instances, then loop
# through them to retrieve each instance and print its instance path and
# properties.
#

import sys
import pywbem

server_url = 'https://server'
user = 'root'
password = 'penguin'

conn = pywbem.WBEMConnection(server_url, (user, password))

try:
    os_paths = conn.EnumerateInstanceNames('CIM_OperatingSystem')
except pywbem.Error as exc:
    print('Error: EnumerateInstanceNames failed: %s' % exc)
    sys.exit(1)

for os_path in os_paths:

    print('Instance at: %s' % os_path)

    try:
        os_inst = conn.GetInstance(os_path)
    except pywbem.Error as exc:
        print('Error: GetInstance failed: %s' % exc)
        sys.exit(1)

    for prop_name, prop_value in os_inst.items():
        print('  %s: %r' % (prop_name, prop_value))

