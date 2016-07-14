#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Control the amount of context by passing a number as arg on command line
"""

import cgitb
import sys

context_length = int(sys.argv[1])
cgitb.enable(format='text', context=context_length)

def func2(a, divisor):
    return a / divisor

def func1(a, b):
    c = b - 5
    # Really
    # long
    # comment
    # goes
    # here.
    return func2(a, c)

func1(1, 5)
