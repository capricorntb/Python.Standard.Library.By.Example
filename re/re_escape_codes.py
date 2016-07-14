#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Escape codes
"""

from re_test_patterns import test_patterns

test_patterns(
    'A prime #1 example!',
    [ (r'\d+', 'sequence of digits'),
      (r'\D+', 'sequence of nondigits'),
      (r'\s+', 'sequence of whitespace'),
      (r'\S+', 'sequence of nonwhitespace'),
      (r'\w+', 'alphanumeric characters'),
      (r'\W+', 'nonalphanumeric'),
      ])
