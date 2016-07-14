#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Checking exit codes from external processes
"""

import subprocess

try:
    subprocess.check_call(['false'])
except subprocess.CalledProcessError as err:
    print 'ERROR:', err
