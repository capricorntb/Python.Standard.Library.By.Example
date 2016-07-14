#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Creating XML documents with lists of nodes
"""

from xml.etree.ElementTree import Element, tostring
from ElementTree_pretty import prettify

top = Element('top')

children = [
    Element('child', num=str(i))
    for i in xrange(3)
    ]

top.extend(children)

print prettify(top)
