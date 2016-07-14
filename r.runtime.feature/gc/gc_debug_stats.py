#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tuning the garbage collector threshold.
"""

import gc

gc.set_debug(gc.DEBUG_STATS)

gc.collect()
