#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Find the directory portion of a filename.
"""

__version__ = "$Id$"

import os.path

for path in [ '/one/two/three', 
              '/one/two/three/',
              '/',
              '.',
              '']:
    print '%15s : %s' % (path, os.path.dirname(path))
