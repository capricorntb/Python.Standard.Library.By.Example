#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Expand shell variables in filenames.
"""

__version__ = "$Id$"

import os.path
import os

os.environ['MYVAR'] = 'VALUE'

print os.path.expandvars('/path/to/$MYVAR')
