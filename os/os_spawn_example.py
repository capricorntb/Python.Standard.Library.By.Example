#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Using spawn*() instead of fork() and exec*().

"""

__module_id__ = "$Id$"

import os

os.spawnlp(os.P_WAIT, 'pwd', 'pwd', '-P')
