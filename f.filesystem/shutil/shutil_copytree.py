#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Copying an entire tree of files.

"""

from shutil import *
from commands import *

print 'BEFORE:'
print getoutput('ls -rlast /tmp/example')
copytree('../shutil', '/tmp/example')
print '\nAFTER:'
print getoutput('ls -rlast /tmp/example')
