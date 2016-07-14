#!/usr/bin/env python
# -*- coding: utf-8 -*-

import bz2
import contextlib
import itertools
import os

with contextlib.closing(bz2.BZ2File('lines.bz2', 'wb')) as output:
    output.writelines(
        itertools.repeat('The same line, over and over.\n', 10),
        )

os.system('bzcat lines.bz2')
