#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Using izip()

"""

from itertools import *

for i in izip([1, 2, 3], ['a', 'b', 'c']):
    print i
