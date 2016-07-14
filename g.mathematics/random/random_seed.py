#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Generate random numbers
"""

import random

random.seed(1)

for i in xrange(5):
    print '%04.3f' % random.random(),
print

