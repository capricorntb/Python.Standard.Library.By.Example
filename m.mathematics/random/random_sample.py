#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Sampling from sequences
"""

import random

with open('/usr/share/dict/words', 'rt') as f:
    words = f.readlines()
words = [ w.rstrip() for w in words ]

for w in random.sample(words, 5):
    print w
    
