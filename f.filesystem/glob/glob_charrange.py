#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Using character range in patterns.
"""

import glob
for name in glob.glob('dir/*[0-9].*'):
    print name
