#!/usr/bin/python
#
# 06-invokemethod.py    Demonstrate invoking a WBEM extrinsic method
#
# See other examples at http://pywbem.sourceforge.net/examples
#

import sys, pywbem

# Make connection

conn = pywbem.WBEMConnection('https://server',     # url
                             ('root', 'penguin'))  # credentials

# Call a method on a class

try:

    conn.InvokeMethod('Foo',
                      pywbem.CIMLocalClassPath('root/cimv2',
                                               'CIM_OperatingSystem'))
except pywbem.CIMError, arg:

    if arg[0] != pywbem.CIM_ERR_NOT_SUPPORTED:
        print 'InvokeMethod(class): %s' % arg[1]
        sys.exit(1)

# Call a method on an instance name

names = conn.EnumerateInstanceNames('CIM_OperatingSystem')

try:

    conn.InvokeMethod('Foo', 
                      pywbem.CIMLocalInstancePath('root/cimv2', names[0]))

except pywbem.CIMError, arg:

    if arg[0] != pywbem.CIM_ERR_NOT_SUPPORTED:
        print 'InvokeMethod(instancename): %s' % arg[1]
        sys.exit(1)
