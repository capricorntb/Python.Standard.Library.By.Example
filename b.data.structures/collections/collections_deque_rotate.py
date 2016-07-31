#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Manipulating the order of items in a deque.
"""

import collections

d = collections.deque(xrange(10))
print 'Normal        :', d

d = collections.deque(xrange(10))
d.rotate(1)
print 'Right rotation:', d

d = collections.deque(xrange(10))
d.rotate(2)
print 'Right rotation:', d

d = collections.deque(xrange(10))
d.rotate(-1)
print 'Left rotation :', d

d = collections.deque(xrange(10))
d.rotate(-2)
print 'Left rotation :', d
