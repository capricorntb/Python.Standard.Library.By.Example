#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Simple example with urllib.urlopen().
"""

import urllib

response = urllib.urlopen('http://localhost:8080/')
for line in response:
    print line.rstrip()
