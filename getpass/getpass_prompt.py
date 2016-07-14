#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Passing a prompt to getpass.

"""

import getpass

p = getpass.getpass(prompt='What is your favorite color? ')
if p.lower() == 'blue':
    print 'Right.  Off you go.'
else:
    print 'Auuuuugh!'

