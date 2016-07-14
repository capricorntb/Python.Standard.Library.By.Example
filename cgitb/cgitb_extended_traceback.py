#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Generate a traceback with more details.
"""

import cgitb
cgitb.enable(format='text')

def func1(arg1):
    local_var = arg1 * 2
    return func2(local_var)

def func2(arg2):
    local_var = arg2 + 2
    return func3(local_var)

def func3(arg3):
    local_var = arg2 / 2
    return local_var

func1(1)
