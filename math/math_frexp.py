#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Separate mantissa from exponent.
"""

import math

print '{:^7}  {:^7}  {:^7}'.format('x', 'm', 'e')
print '{:-^7}  {:-^7}  {:-^7}'.format('', '', '')

for x in [ 0.1, 0.5, 4.0 ]:
    m, e = math.frexp(x)
    print '{:7.2f}  {:7.2f}  {:7d}'.format(x, m, e)
