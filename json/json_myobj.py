#!/usr/bin/env python
# -*- coding: utf-8 -*-

class MyObj(object):
    def __init__(self, s):
        self.s = s
    def __repr__(self):
        return '<MyObj(%s)>' % self.s
