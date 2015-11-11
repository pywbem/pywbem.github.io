#!/usr/bin/python
#
# 00-connect.py    Demonstrate making WBEM connections.
#
# See other examples at http://pywbem.sourceforge.net/examples
#

import pywbem

# Make connection

conn = pywbem.WBEMConnection('https://server',     # url
                             ('root', 'penguin'))  # credentials
