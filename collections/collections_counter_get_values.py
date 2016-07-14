#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Updating counts.
"""

import collections

c = collections.Counter('abcdaab')

for letter in 'abcde':
    print '%s : %d' % (letter, c[letter])

