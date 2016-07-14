#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Simplistic examples of unit tests.

"""

import unittest

class SimplisticTest(unittest.TestCase):

    def test(self):
        self.failUnless(True)

if __name__ == '__main__':
    unittest.main()
