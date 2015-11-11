#!/usr/bin/python
#
# Check that the properties of instances of a class correspond to the
# definition for that class.
#
# (c) 2005, Tim Potter <tpot@hp.com> under the GNU GPL.
#

import sys
import pywbem

# Command line args

if len(sys.argv) != 5:
    print 'Usage: instance-checker.py SERVER USERNAME PASSWORD CLASSNAME'
    sys.exit(0)

server  = sys.argv[1]
username, password = sys.argv[2:4]
classname = sys.argv[4]

# Make WBEM connection

conn = pywbem.WBEMConnection('https://%s' % server, (username, password))

# Get class definition and instances of class

klass = conn.GetClass(classname)
instances = conn.EnumerateInstances(classname)

# Check instances aginst class definition

for i in instances:

    # Check for extra properties

    extra = set(klass.properties.keys()) - set(i.properties.keys())

    if len(extra) > 0:
        print 'Extra properties in %s instance: %s' % (classname, extra) 

    # Check for missing properties

    missing = set(i.properties.keys()) - set(klass.properties.keys())

    if len(missing) > 0:
        print 'Missing properties in %s instances: %s' % (classname, missing)

    # Check property types against definition

    for prop, value in i.properties.items():

        if not klass.properties.has_key(prop):
            continue

        if value.type != klass.properties[prop].type:
            print 'Property %s has incorrect type' % \
                  klass.properties[key].name
