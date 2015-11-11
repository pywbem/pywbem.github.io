#!/usr/bin/python
#
# 01-enumerate-instances.py    Demonstrate enumeration of instances
#
# See other examples at http://pywbem.sourceforge.net/examples
#

import pywbem

# Make connection

conn = pywbem.WBEMConnection('https://server',     # url
                             ('root', 'penguin'))  # credentials

# Enumerate CIM_Process instance names and instances

instance_names = conn.EnumerateInstanceNames('CIM_Process')
instances = conn.EnumerateInstance('CIM_Process')

print '%d CIM_Process names returned' % len(instance_names)
print '%d CIM_Process instances returned' % len(instance_names)
