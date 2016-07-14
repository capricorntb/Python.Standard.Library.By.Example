#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Examine the objects being managed.
"""

import gc

print len(gc.get_objects())
