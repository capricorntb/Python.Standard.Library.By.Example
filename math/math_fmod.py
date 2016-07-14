#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Floating point modulo
"""

import math

print '{:^4}  {:^4}  {:^5}  {:^5}'.format('x', 'y', '%', 'fmod')
print '----  ----  -----  -----'

for x, y in [ (5, 2),
              (5, -2),
              (-5, 2),
              ]:
    print '{:4.1f}  {:4.1f}  {:5.2f}  {:5.2f}'.format(
        x,
        y,
        x % y,
        math.fmod(x, y),
        )
