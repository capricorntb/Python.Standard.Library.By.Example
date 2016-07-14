#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Look up a hostname from its address.
"""

import socket

hostname, aliases, addresses = socket.gethostbyaddr('192.168.1.8')

print 'Hostname :', hostname
print 'Aliases  :', aliases
print 'Addresses:', addresses
