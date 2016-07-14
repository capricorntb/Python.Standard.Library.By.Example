#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Example use of popen() varients from os.

"""

# Ignore deprecation warnings
import warnings
warnings.filterwarnings('ignore', 'os.popen.* is deprecated.*',)

import os

print 'popen3:'
stdin, stdout, stderr = os.popen3('cat -; echo ";to stderr" 1>&2')
try:
    stdin.write('through stdin to stdout')
finally:
    stdin.close()
try:
    stdout_value = stdout.read()
finally:
    stdout.close()
print '\tpass through:', repr(stdout_value)
try:
    stderr_value = stderr.read()
finally:
    stderr.close()
print '\tstderr:', repr(stderr_value)
