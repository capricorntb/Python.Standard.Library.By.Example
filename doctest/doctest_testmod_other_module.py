#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Run tests for another module we import.
"""

import doctest_simple

if __name__ == '__main__':
    import doctest
    doctest.testmod(doctest_simple)
    
