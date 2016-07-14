#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Writing Unicode data to a file.
"""

import codecs
import sys

encoding = sys.argv[1]
filename = encoding + '.txt'

print 'Reading from', filename
with codecs.open(filename, mode='rt', encoding=encoding) as f:
    print repr(f.read())
