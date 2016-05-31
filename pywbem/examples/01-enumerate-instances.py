#!/usr/bin/env python
#
# Demonstrate enumeration of instances.
#

import pywbem

server_url = 'https://server'
user = 'root'
password = 'penguin'

conn = pywbem.WBEMConnection(server_url, (user, password))

try:
    proc_paths = conn.EnumerateInstanceNames('CIM_Process')
except pywbem.Error as exc:
    print('Error: EnumerateInstanceNames failed: %s' % exc)
    sys.exit(1)

print('%d CIM_Process instance paths returned' % len(proc_paths))

try:
    proc_insts = conn.EnumerateInstances('CIM_Process')
except pywbem.Error as exc:
    print('Error: EnumerateInstances failed: %s' % exc)
    sys.exit(1)

print('%d CIM_Process instances returned' % len(proc_insts))

