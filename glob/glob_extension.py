#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Using glob to find files matching a pattern with a filename extension.
"""

import glob

for name in glob.glob('*.py'):
    print name
