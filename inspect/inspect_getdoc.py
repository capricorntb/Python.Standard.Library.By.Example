#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Docstrings

"""

import inspect
import example

print 'B.__doc__:'
print example.B.__doc__
print
print 'getdoc(B):'
print inspect.getdoc(example.B)
