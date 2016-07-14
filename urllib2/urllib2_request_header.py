#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Simple example with urllib2.urlopen().
"""

import urllib2

request = urllib2.Request('http://localhost:8080/')
request.add_header(
    'User-agent',
    'PyMOTW (http://www.doughellmann.com/PyMOTW/)',
    )

response = urllib2.urlopen(request)
data = response.read()
print data
