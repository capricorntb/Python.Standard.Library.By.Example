#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

print 'The time is      :', time.ctime()
later = time.time() + 15
print '15 secs from now :', time.ctime(later)
