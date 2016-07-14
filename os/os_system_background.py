#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Running a command in the background

"""

__module_id__ = "$Id$"

import os
import time

print 'Calling...'
os.system('date; (sleep 3; date) &')

print 'Sleeping...'
time.sleep(5)
