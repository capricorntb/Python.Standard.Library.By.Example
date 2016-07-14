#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Produce the elements of the counter.
"""

import collections

c = collections.Counter('extremely')
c['z'] = 0
print c
print list(c.elements())
