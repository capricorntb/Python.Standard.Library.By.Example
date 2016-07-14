#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Generate random numbers
"""

import random

for i in xrange(5):
    print '%04.3f' % random.uniform(1, 100),
print

