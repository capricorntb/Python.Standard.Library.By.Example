#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Register repeatedly with different arguments.

"""

import atexit

def my_cleanup(name):
    print 'my_cleanup(%s)' % name

atexit.register(my_cleanup, 'first')
atexit.register(my_cleanup, 'second')
atexit.register(my_cleanup, 'third')
