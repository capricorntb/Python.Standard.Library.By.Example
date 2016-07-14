#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Repetition of patterns
"""

from re_test_patterns import test_patterns

test_patterns(
    'This is some text -- with punctuation.',
    [ ('[^-. ]+',  'sequences without -, ., or space'),
      ])
