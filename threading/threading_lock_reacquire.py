#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Normal locks cannot be acquired more than once, even by the same thread
"""

import threading

lock = threading.Lock()

print 'First try :', lock.acquire()
print 'Second try:', lock.acquire(0)
