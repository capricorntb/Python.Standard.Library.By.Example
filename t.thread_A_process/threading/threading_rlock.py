#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Re-entrant locks
"""

import threading

lock = threading.RLock()

print 'First try :', lock.acquire()
print 'Second try:', lock.acquire(0)
