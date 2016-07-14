#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Using os.system() to run external commands.
"""

import os

# Command with shell expansion
os.system('echo $TMPDIR')
