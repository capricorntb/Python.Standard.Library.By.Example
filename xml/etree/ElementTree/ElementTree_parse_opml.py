#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Parse the input OPML file and show something about the results.
"""

from xml.etree import ElementTree

with open('podcasts.opml', 'rt') as f:
    tree = ElementTree.parse(f)

print tree



