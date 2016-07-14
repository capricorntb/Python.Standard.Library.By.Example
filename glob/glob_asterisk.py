#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    The asterisk as wildcard character.
"""

import glob
for name in glob.glob('dir/*'):
    print name
