#!/usr/bin/env python
#
# Demonstrate deleting CIM instances.
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

try:
    conn.DeleteInstance(os_paths[0])
except pywbem.Error as exc:
    if isinstance(exc, pywbem.CIMError) and exc[0] == pywbem.CIM_ERR_NOT_SUPPORTED:
        # A CIM error "not supported" is OK as the operating system provider
        # should not support deletion
        pass
    else:
        print('Error: DeleteInstance failed: %s' % exc)
        sys.exit(1)

