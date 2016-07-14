#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xmlrpclib

server = xmlrpclib.ServerProxy('http://localhost:9000',
                               encoding='ISO-8859-1')
print 'Ping:', server.ping()
