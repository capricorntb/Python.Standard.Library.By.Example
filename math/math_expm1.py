#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Logarithms close to zero.
"""

import math

x = 0.0000000000000000000000001

print x
print math.exp(x) - 1
print math.expm1(x)
