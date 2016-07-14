#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Using count()

"""

from itertools import *

for i in izip(count(1), ['a', 'b', 'c']):
    print i
