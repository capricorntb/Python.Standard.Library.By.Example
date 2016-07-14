#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Using repeat() with izip().

"""

from itertools import *

for i, s in izip(count(), repeat('over-and-over', 5)):
    print i, s
