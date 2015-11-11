#!/usr/bin/python
#
# 03-deleteinstance.py    Demonstrate deleting WBEM objects
#
# See other examples at http://pywbem.sourceforge.net/examples
#

import sys, pywbem

# Make connection

conn = pywbem.WBEMConnection('https://server',     # url
                             ('root', 'penguin'))  # credentials

# Try to delete the CIM_OperatingSystem instance

names = conn.EnumerateInstanceNames('CIM_OperatingSystem')

try:

    conn.DeleteInstance(names[0])

except pywbem.CIMError, arg:

    # A not supported error is OK as the operating system provider should
    # not support deletion

    if arg[0] != pywbem.CIM_ERR_NOT_SUPPORTED:
        print 'DeleteInstance: %s' % arg[1]
        sys.exit(1)
