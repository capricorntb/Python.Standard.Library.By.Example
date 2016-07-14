#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Dump the OPML in plain text
"""

from xml.etree import ElementTree

with open('podcasts.opml', 'rt') as f:
    tree = ElementTree.parse(f)

for node in tree.findall('.//outline/outline'):
    url = node.attrib.get('xmlUrl')
    print url
