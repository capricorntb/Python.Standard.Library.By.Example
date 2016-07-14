#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xmlrpclib

server = xmlrpclib.ServerProxy('http://localhost:9000',
                               allow_none=True)
print 'Allowed:', server.show_type(None)

server = xmlrpclib.ServerProxy('http://localhost:9000',
                               allow_none=False)
try:
    server.show_type(None)
except TypeError as err:
    print 'ERROR:', err
    
