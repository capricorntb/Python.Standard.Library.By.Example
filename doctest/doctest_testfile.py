#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Run the tests from an external file.
"""

import doctest

if __name__ == '__main__':
    doctest.testfile('doctest_in_help.rst')
    
