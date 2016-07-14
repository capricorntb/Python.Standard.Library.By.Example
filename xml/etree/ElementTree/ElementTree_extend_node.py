#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Creating XML documents with lists of nodes
"""

from xml.etree.ElementTree import Element, SubElement, tostring, XML
from ElementTree_pretty import prettify

top = Element('top')

parent = SubElement(top, 'parent')

children = XML(
   '<root><child num="0" /><child num="1" /><child num="2" /></root>'
   )
parent.extend(children)

print prettify(top)

