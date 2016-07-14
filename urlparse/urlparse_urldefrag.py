#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Remove fragment portion of URL
"""

from urlparse import urldefrag

original = 'http://netloc/path;param?query=arg#frag'
print 'original:', original
url, fragment = urldefrag(original)
print 'url     :', url
print 'fragment:', fragment
