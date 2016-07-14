#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Using spawn*() instead of fork() and exec*().
"""

import os

os.spawnlp(os.P_WAIT, 'pwd', 'pwd', '-P')
