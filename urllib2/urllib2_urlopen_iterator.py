#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Simple example with urllib.urlopen().
"""

import urllib2

response = urllib2.urlopen('http://localhost:8080/')
for line in response:
    print line.rstrip()
