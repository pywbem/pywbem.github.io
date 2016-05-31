#!/usr/bin/env python
#
# Demonstrate modification of CIM instances.
#
import sys
import pywbem

server_url = 'https://server'
user = 'root'
password = 'penguin'

conn = pywbem.WBEMConnection(server_url, (user, password))

filter_inst = pywbem.CIMInstance(
    'CIM_IndicationFilter',
    {'Name': 'pywbem_test',
     'Query': 'SELECT * FROM CIM_Indication',
     'QueryLanguage': 'WQL'})

try:
    filter_path = conn.CreateInstance(filter_inst)
except pywbem.Error as exc:
    print('Error: CreateInstance failed: %s' % exc)
    sys.exit(1)

filter_inst['Query'] = 'SELECT * FROM CIM_ProcessIndication'

try:
    conn.ModifyInstance(filter_path, filter_inst)
except pywbem.Error as exc:
    if isinstance(exc, pywbem.CIMError) and exc[0] == pywbem.CIM_ERR_NOT_SUPPORTED:
        # If the WBEM server doesn't support modification of CIM_IndicationFilter
        # we ignore this error for the purposes of the example.
        print('Modifying CIM_IndicationFilter is not supported')
    else:
        print('Error: ModifyInstance failed: %s' % exc)
        sys.exit(1)

try:
    conn.DeleteInstance(filter_path)
except pywbem.Error as exc:
    print('Error: DeleteInstance failed: %s' % exc)
    sys.exit(1)

