#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Example use of popen() varients from os.

"""

# Ignore deprecation warnings
import warnings
warnings.filterwarnings('ignore', 'os.popen.* is deprecated.*',)

import os

print 'popen4:'
stdin, stdout_and_stderr = os.popen4('cat -; echo ";to stderr" 1>&2')
try:
    stdin.write('through stdin to stdout')
finally:
    stdin.close()
try:
    stdout_value = stdout_and_stderr.read()
finally:
    stdout_and_stderr.close()
print '\tcombined output:', repr(stdout_value)
