#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Long option name example.
"""

import argparse

parser = argparse.ArgumentParser(
    description='Example with nonoptional arguments',
    )

parser.add_argument('count', action="store", type=int)
parser.add_argument('units', action="store")

print parser.parse_args()
