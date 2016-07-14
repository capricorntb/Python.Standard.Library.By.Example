#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Compute a "normalized" path.
"""

__version__ = "$Id$"

import os.path

for path in [ 'one//two//three', 
              'one/./two/./three', 
              'one/../alt/two/three',
              ]:
    print '%20s : %s' % (path, os.path.normpath(path))
