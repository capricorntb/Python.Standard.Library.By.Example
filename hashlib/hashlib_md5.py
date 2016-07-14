#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Simple MD5 generation.
"""

import hashlib

from hashlib_data import lorem

h = hashlib.md5()
h.update(lorem)
print h.hexdigest()
