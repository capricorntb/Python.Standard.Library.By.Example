#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""LIFO Queue
"""

import Queue

q = Queue.LifoQueue()

for i in range(5):
    q.put(i)

while not q.empty():
    print q.get(),
print
