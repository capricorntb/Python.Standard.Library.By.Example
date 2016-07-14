#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Passing arguments to threads when they are created
"""

import threading

def worker(num):
    """thread worker function"""
    print 'Worker: %s' % num
    return

threads = []
for i in range(5):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()
