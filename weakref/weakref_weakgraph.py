#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tools for demonstrating garbage collection
"""

import gc
from pprint import pprint
import weakref

from weakref_graph import Graph, demo

class WeakGraph(Graph):
    def set_next(self, other):
        if other is not None:
            # See if we should replace the reference
            # to other with a weakref.
            if self in other.all_nodes():
                other = weakref.proxy(other)
        super(WeakGraph, self).set_next(other)
        return
                
demo(WeakGraph)
