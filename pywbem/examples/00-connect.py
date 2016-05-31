#!/usr/bin/env python
#
# Demonstrate making WBEM connections.
#

import pywbem

server_url = 'https://server'
user = 'root'
password = 'penguin'

conn = pywbem.WBEMConnection(server_url, (user, password))

