#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Example use of ConfigParser module.

See http://blog.doughellmann.com/2007/04/pymotw-configparser.html

"""

from ConfigParser import ConfigParser
import os

filename = 'approach.ini'
config = ConfigParser()
config.read([filename])

url = config.get('portal', 'url')

print url
