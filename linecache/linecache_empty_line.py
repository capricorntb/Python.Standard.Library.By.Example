#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Example use of linecache module.
"""

import linecache
from linecache_data import *

filename = make_tempfile()

# Blank lines include the newline
print 'BLANK : %r' % linecache.getline(filename, 8)

cleanup(filename)
