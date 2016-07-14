#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Repetition of patterns
"""

from re_test_patterns import test_patterns

test_patterns(
    'abbaabbba',
    [ ('[ab]',    'either a or b'),
      ('a[ab]+',  'a followed by 1 or more a or b'),
      ('a[ab]+?', 'a followed by 1 or more a or b, not greedy'),
      ])
