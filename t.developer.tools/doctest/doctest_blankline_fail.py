#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Blank lines in the input cause mis-matches.
"""

def double_space(lines):
    """Prints a list of lines double-spaced.

    >>> double_space(['Line one.', 'Line two.'])
    Line one.
    
    Line two.
    
    """
    for l in lines:
        print l
        print
    return


