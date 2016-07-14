#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Using getmembers()

"""

import inspect
from pprint import pprint

import example

a = example.A(name='inspect_getmembers')
pprint(inspect.getmembers(a))
