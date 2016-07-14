#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Raise e to a power.
"""

import math

x = 2

fmt = '%.20f'
print fmt % (math.e ** 2)
print fmt % math.pow(math.e, 2)
print fmt % math.exp(2)
