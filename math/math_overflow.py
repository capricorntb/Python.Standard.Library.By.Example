#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""OverflowError
"""

x = 10.0 ** 200

print 'x    =', x
print 'x*x  =', x*x
try:
    print 'x**2 =', x**2
except OverflowError, err:
    print err
