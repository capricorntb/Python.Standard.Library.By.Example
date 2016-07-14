#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Joining relative fragments into absolute URLs
"""

from urlparse import urljoin

print urljoin('http://www.example.com/path/file.html',
              'anotherfile.html')
print urljoin('http://www.example.com/path/file.html',
              '../anotherfile.html')
