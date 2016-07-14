#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Capture the output of a command and test its exit code at the same time.
"""

import subprocess

output = subprocess.check_output(['ls', '-1'])
print 'Have %d bytes in output' % len(output)
print output

                                  
