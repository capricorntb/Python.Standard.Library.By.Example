#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Remove an entire tree of files.

"""

from shutil import *
from commands import *

print 'BEFORE:'
print getoutput('ls -rlast /tmp/example')
rmtree('/tmp/example')
print 'AFTER:'
print getoutput('ls -rlast /tmp/example')
