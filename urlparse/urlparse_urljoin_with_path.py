#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Joining fragments into absolute URLs
"""

from urlparse import urljoin

print urljoin('http://www.example.com/path/',
              '/subpath/file.html')
print urljoin('http://www.example.com/path/',
              'subpath/file.html')
