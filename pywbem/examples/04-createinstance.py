#!/usr/bin/env python
#
# Demonstrate creation of CIM instances.
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

try:
    conn.DeleteInstance(filter_path)
except pywbem.Error as exc:
    print('Error: DeleteInstance failed: %s' % exc)
    sys.exit(1)

