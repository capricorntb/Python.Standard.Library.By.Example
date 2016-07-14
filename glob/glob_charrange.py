#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Using character range in patterns.

"""

__module_id__ = "$Id$"

import glob
for name in glob.glob('dir/*[0-9].*'):
    print name
