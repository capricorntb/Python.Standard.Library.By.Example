#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Translate a glob-style pattern to a regular expression.
"""

import fnmatch

pattern = 'fnmatch_*.py'
print 'Pattern :', pattern
print 'Regex   :', fnmatch.translate(pattern)
