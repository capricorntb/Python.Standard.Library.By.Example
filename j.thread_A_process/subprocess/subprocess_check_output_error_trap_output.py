#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Capture the output of a command and test its exit code at the same time.
"""

import subprocess

try:
    output = subprocess.check_output(
        'echo to stdout; echo to stderr 1>&2; exit 1',
        shell=True,
        stderr=subprocess.STDOUT,
        )
except subprocess.CalledProcessError as err:
    print 'ERROR:', err
else:
    print 'Have %d bytes in output' % len(output)
    print output

                                  
