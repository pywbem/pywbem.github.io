#!/usr/bin/python
#
# A simple CGI schema browser.
#
# Run like 'thttps -h localhost -p 8000 -c \*.cgi' and point your browser
# at http://localhost:8000/schema-browser.py to run, or figure out how to
# install it under Apache yourself.
#
# (c) 2005, Tim Potter <tpot@hp.com> under the GNU GPL.
#

import sys, cgi
import pywbem

# Hardcoded connection details for now

server = 'server'
creds = ('root', 'penguin')

# Make WBEM connection

conn = pywbem.WBEMConnection('https://%s' % server, creds)

# HTTP header

print 'Content-Type: text/html\n'

# Start HTML

print '<html><head>'
print '<title>schema-browser.py</title>'
print '</head><body>'

# Body

form = cgi.FormContentDict()

if form.has_key('classname'):

    # Header

    classname = form['classname'][0]

    print '<h1>%s</h1>' % classname

    # Get class info

    try:
        cl = conn.GetClass(classname,
                           LocalOnly = False)
    except pywbem.CIMError, arg:
        print arg[1]
        sys.exit(0)

    # Qualifiers

    print '<dl>'

    print '<dt><b>Superclass</b><dd><a href="?classname=%s">%s</a><p>' % \
          (cl.superclass, cl.superclass)

    [sys.stdout.write('<dt><b>%s</b><dd>%s<p>' % (q.name, q.value))
     for q in cl.qualifiers.values()]

    print '</dl>'
                      
    # Display key properties

    print '<h2>Key Properties</h2>'

    print '<ul>'

    [sys.stdout.write('<li><tt>%s</tt><p>%s' % \
                      (key, value.qualifiers['Description'].value))
     for key, value in cl.properties.items()
     if value.qualifiers.has_key('Key')]

    print '</ul>'

    # Display properties

    print '<h2>Properties</h2>'

    print '<ul>'

    [sys.stdout.write('<li><tt>%s</tt><p>%s' % \
                      (key, value.qualifiers['Description'].value))
     for key, value in cl.properties.items()
     if not value.qualifiers.has_key('Key')]

    print '</ul>'

else:

    # Display list of classnames

    classnames = conn.EnumerateClassNames(DeepInheritance = True)
    classnames.sort()

    print '<h1>Classes</h1>'

    print '<ul>'

    [sys.stdout.write('<li><a href="?classname=%s">%s</a>' % (cl, cl))
     for cl in classnames]

    print '</ul>'

# End HTML

print '</body></html>'
