#!/usr/bin/env python
# -*- coding: utf-8 -*-

import inspect
import pprint
import example

pprint.pprint(inspect.getsourcelines(example.A.get_name))
