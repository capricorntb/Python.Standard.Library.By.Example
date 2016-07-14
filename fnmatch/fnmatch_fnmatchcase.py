#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Force a case-sensitive test of a filename with a pattern.
"""

import fnmatch
import os

pattern = 'FNMATCH_*.PY'
print 'Pattern :', pattern
print

files = os.listdir('.')

for name in files:
    print 'Filename: %-25s %s' % \
        (name, fnmatch.fnmatchcase(name, pattern))
