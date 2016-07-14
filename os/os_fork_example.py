#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Simple example of using os.fork to create a new child process.
"""

import os

pid = os.fork()

if pid:
    print 'Child process id:', pid
else:
    print 'I am the child'
