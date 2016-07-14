#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Creating and waiting for a thread.
"""

import threading

def worker():
    """thread worker function"""
    print 'Worker'
    return

threads = []
for i in range(5):
    t = threading.Thread(target=worker)
    threads.append(t)
    t.start()
