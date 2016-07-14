#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""AttributeError from class that uses __slots__
"""

class MyClass(object):
    __slots__ = ( 'attribute', )

o = MyClass()
o.attribute = 'known attribute'
o.not_a_slot = 'new attribute'

