#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Parent with shared options
"""

import argparse
import argparse_parent_with_group

parser = argparse.ArgumentParser(
    parents=[argparse_parent_with_group.parser],
    )

parser.add_argument('--local-arg',
                    action="store_true",
                    default=False)

print parser.parse_args()
