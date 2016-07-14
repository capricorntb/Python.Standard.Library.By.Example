#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Show how values map to function arguments.
"""

import inspect
import example
import pprint

for args, kwds in [
    (('a',), {'unknown_name':'value'}),
    (('a',), {'arg2':'value'}),
    (('a', 'b', 'c', 'd'), {}),
    ((), {'arg1':'a'}),
    ]:
    print args, kwds
    callargs = inspect.getcallargs(example.module_level_function,
                                   *args, **kwds)
    pprint.pprint(callargs, width=74)
    example.module_level_function(**callargs)
    print
