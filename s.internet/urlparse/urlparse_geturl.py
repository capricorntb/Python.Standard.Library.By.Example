#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Parsing URLs
"""

from urlparse import urlparse

original = 'http://netloc/path;param?query=arg#frag'
print 'ORIG  :', original
parsed = urlparse(original)
print 'PARSED:', parsed.geturl()
