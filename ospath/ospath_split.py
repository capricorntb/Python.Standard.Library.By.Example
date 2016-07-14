#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Separate a path into its directory and base components.
"""

__version__ = "$Id$"

import os.path

for path in [ '/one/two/three', 
              '/one/two/three/',
              '/',
              '.',
              '']:
    print '%15s : %s' % (path, os.path.split(path))
