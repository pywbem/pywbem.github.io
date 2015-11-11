#!/usr/bin/python
#
# 04-modifyinstance.py    Demonstrate modification of WBEM objects
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

# Modify the CIM_IndicationFilter instance

filter['Query'] = 'SELECT * FROM CIM_ProcessIndication'

try:

    new_filter_name = conn.ModifyInstance(filter_name, filter)

except pywbem.CIMError, arg:

    # OpenPegasus doesn't support modification of CIM_IndicationFilter
    # so just ignore this error for the purposes of the example.

    if arg[0] != pywbem.CIM_ERR_NOT_SUPPORTED:
        print 'ModifyInstance: %s' % msg[1]

    conn.DeleteInstance(filter_name)

else:
    conn.DeleteInstance(new_filter_name)
