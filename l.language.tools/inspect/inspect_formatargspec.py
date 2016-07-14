#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Print information about the arguments to a method.

"""

import inspect
import example

spec = inspect.getargspec(example.module_level_function)
print spec
print inspect.formatargspec(spec)
