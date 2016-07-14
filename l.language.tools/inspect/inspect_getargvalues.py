#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Inspecting the call stack.

"""

import inspect

def recurse(limit):
    local_variable = '.' * limit
    print limit, inspect.getargvalues(inspect.currentframe())
    if limit <= 0:
        return
    recurse(limit - 1)
    return

if __name__ == '__main__':
    recurse(2)
