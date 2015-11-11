#!/usr/bin/python
#
# 02-getinstance.py    Demonstrate calling GetInstance
#
# See other examples at http://pywbem.sourceforge.net/examples
#

import pywbem

# Make connection

conn = pywbem.WBEMConnection('https://server',     # url
                             ('root', 'penguin'))  # credentials

# Get all CIM_OperatingSystem instances

names = conn.EnumerateInstanceNames('CIM_OperatingSystem')

# Call GetInstance on returned instances

for n in names:

    os = conn.GetInstance(n)

    for key, value in os.items():
        print '%s = %s' % (key, value)
