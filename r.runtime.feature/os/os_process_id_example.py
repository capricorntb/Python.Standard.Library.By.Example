#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Using the os module to find information about the current process.
"""

import os

print 'This process id:', os.getpid()
print 'Parent process :', os.getppid()
print 'Process group  :', os.getpgid(os.getpid())
print 'Parent group   :', os.getpgid(os.getppid())
print 'Session id     :', os.getsid(0)
