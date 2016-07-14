#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Parent with shared options
"""

import argparse

parser = argparse.ArgumentParser(add_help=False)

parser.add_argument('--user', action="store")
parser.add_argument('--password', action="store")
