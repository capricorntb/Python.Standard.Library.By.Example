#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Using getmembers()

"""

import inspect
from pprint import pprint

import example

pprint(inspect.getmembers(example.B, inspect.ismethod))
