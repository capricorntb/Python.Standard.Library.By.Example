#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Escaping escape codes
"""

from re_test_patterns import test_patterns

test_patterns(
    r'\d+ \D+ \s+',
    [ (r'\\.\+', 'escape code'),
      ])
