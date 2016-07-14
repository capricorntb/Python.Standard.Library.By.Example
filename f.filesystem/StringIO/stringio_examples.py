#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Simple examples with StringIO module

    See http://blog.doughellmann.com/2007/04/pymotw-stringio-and-cstringio.html

"""

# Find the best implementation available on this platform
try:
    from cStringIO import StringIO
except:
    from StringIO import StringIO

# Writing to a buffer
output = StringIO()
output.write('This goes into the buffer. ')
print >>output, 'And so does this.'

# Retrieve the value written
print output.getvalue()

output.close() # discard buffer memory

# Initialize a read buffer
input = StringIO('Inital value for read buffer')

# Read from the buffer
print input.read()
