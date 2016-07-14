#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Including content from other files in the token stream.

"""

import shlex

text = """This text says to source quotes.txt before continuing."""
print 'ORIGINAL:', repr(text)
print

lexer = shlex.shlex(text)
lexer.wordchars += '.'
lexer.source = 'source'

print 'TOKENS:'
for token in lexer:
    print repr(token)
