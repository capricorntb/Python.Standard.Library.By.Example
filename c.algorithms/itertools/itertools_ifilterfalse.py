#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Using ifilterfalse()

"""

from itertools import *

def check_item(x):
    print 'Testing:', x
    return (x<1)

for i in ifilterfalse(check_item, [ -1, 0, 1, 2, -2 ]):
    print 'Yielding:', i
