#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Using the os module to read and write environment variables.

"""

__module_id__ = "$Id$"

import os

print 'Initial value:', os.environ.get('TESTVAR', None)
print 'Child process:'
os.system('echo $TESTVAR')

os.environ['TESTVAR'] = 'THIS VALUE WAS CHANGED'

print
print 'Changed value:', os.environ['TESTVAR']
print 'Child process:' 
os.system('echo $TESTVAR')

del os.environ['TESTVAR']

print
print 'Removed value:', os.environ.get('TESTVAR', None)
print 'Child process:' 
os.system('echo $TESTVAR')
