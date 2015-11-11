#!/usr/bin/python
#
# 04-createinstance.py    Demonstrate creation of WBEM objects
#
# See other examples at http://pywbem.sourceforge.net/examples
#

import sys, pywbem

# Make connection

conn = pywbem.WBEMConnection('https://server',     # url
                             ('root', 'penguin'))  # credentials

# Create a CIM_IndicationFilter instance

filter = pywbem.CIMInstance(
    'CIM_IndicationFilter',
    {'Name': 'pywbem_test',
     'Query': 'SELECT * FROM CIM_Indication',
     'QueryLanguage': 'WQL'})

try:

    filter_name = conn.CreateInstance(filter)

except pywbem.CIMError, arg:
    print 'CreateInstance: %s' % arg[1]
    sys.exit(1)

# Be nice and clean it up afterwards

conn.DeleteInstance(filter_name)
