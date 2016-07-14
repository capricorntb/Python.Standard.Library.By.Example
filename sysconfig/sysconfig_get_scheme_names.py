#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Installation schemes.
"""

import sysconfig

for name in sysconfig.get_scheme_names():
    print name
