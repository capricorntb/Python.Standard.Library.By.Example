#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Whitespace at the end of a line can cause a mis-match.
"""

def my_function(a, b):
    """
    >>> my_function(2, 3) #doctest: +REPORT_NDIFF
    6 
    >>> my_function('a', 3)
    'aaa'
    """
    return a * b
