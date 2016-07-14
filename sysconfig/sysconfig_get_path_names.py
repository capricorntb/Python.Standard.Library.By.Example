#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The names of the paths in a scheme.
"""

import sysconfig

for name in sysconfig.get_path_names():
    print name
