#!/usr/bin/env python
#
# Demonstrate invoking methods on CIM classes and on CIM instances.
#

import sys
import pywbem

server_url = 'https://server'
user = 'root'
password = 'penguin'

conn = pywbem.WBEMConnection(server_url, (user, password))

os_class_path = pywbem.CIMClassName('CIM_OperatingSystem', namespace='root/cimv2'))

try:
    result = conn.InvokeMethod('MyStaticMethod', os_class_path)
except pywbem.Error as exc:
    if isinstance(exc, pywbem.CIMError) and exc.status_code == pywbem.CIM_ERR_NOT_SUPPORTED:
        # If the WBEM server doesn't support method invocation,
        # we ignore this error for the purposes of the example.
        print('WBEM server does not support method invocation')
    elif isinstance(exc, pywbem.CIMError) and exc.status_code == CIM_ERR_METHOD_NOT_FOUND:
        # Because the method we used does not exist, we ignore this error.
        pass
    else:
        print('Error: InvokeMethod(MyStaticMethod) failed: %s' % exc)
        sys.exit(1)

try:
    os_inst_paths = conn.EnumerateInstanceNames('CIM_OperatingSystem')
except pywbem.Error as exc:
    print('Error: EnumerateInstanceNames failed: %s' % exc)
    sys.exit(1)

os_inst_path = os_inst_paths[0]

try:
    result = conn.InvokeMethod('MyMethod', os_inst_path)
except pywbem.Error as exc:
    if isinstance(exc, pywbem.CIMError) and exc.status_code == pywbem.CIM_ERR_NOT_SUPPORTED:
        # If the WBEM server doesn't support method invocation,
        # we ignore this error for the purposes of the example.
        print('WBEM server does not support method invocation')
    else:
        print('Error: InvokeMethod(MyMethod) failed: %s' % exc)
        sys.exit(1)

