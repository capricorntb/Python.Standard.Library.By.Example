#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Using cycle().

"""

from itertools import *

for i, item in izip(xrange(7), cycle(['a', 'b', 'c'])):
    print (i, item)
