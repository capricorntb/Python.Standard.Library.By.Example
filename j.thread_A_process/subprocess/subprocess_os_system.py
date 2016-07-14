#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Replacing os.system with subprocess.
"""

import subprocess

# Simple command
subprocess.call(['ls', '-1'])
