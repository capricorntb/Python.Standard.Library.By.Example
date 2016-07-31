#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Count the most common letters in words.
"""

import collections

c = collections.Counter()
#with open('/usr/share/dict/words', 'rt') as f:
with open('collections_counter_most_common.py', 'rt') as f:
    for line in f:
        c.update(line.rstrip().lower())

print 'Most common:'
for letter, count in c.most_common(8):
    print '%s: %7d' % (letter, count)
