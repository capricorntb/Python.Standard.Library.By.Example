#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Combine path components to create a single path.
"""

__version__ = "$Id$"

import os.path

for parts in [ ('one', 'two', 'three'),
               ('/', 'one', 'two', 'three'),
               ('/one', '/two', '/three'),
               ]:
    print parts, ':', os.path.join(*parts)
