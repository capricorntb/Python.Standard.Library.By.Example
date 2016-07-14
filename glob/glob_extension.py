#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Using glob to find files matching a pattern with a filename extension.

"""

__module_id__ = "$Id$"

import glob

for name in glob.glob('*.py'):
    print name
