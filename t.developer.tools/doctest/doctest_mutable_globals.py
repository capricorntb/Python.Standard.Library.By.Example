#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests that modify module-level global values.
"""

_module_data = {}

class TestGlobals(object):

    def one(self):
        """
        >>> TestGlobals().one()
        >>> 'var' in _module_data
        True
        """
        _module_data['var'] = 'value'

    def two(self):
        """
        >>> 'var' in _module_data
        False
        """
    


