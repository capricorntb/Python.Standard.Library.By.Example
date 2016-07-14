#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Logging exceptions to a file, instead of displaying them.
"""

import cgitb
import os

cgitb.enable(logdir=os.path.join(os.path.dirname(__file__), 'LOGS'),
             display=False,
             format='text',
             )

def func(a, divisor):
    return a / divisor

func(1, 0)
