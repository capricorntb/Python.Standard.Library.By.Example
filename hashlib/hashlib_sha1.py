#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Simple SHA1 generation.
"""

import hashlib

from hashlib_data import lorem

h = hashlib.sha1()
h.update(lorem)
print h.hexdigest()
