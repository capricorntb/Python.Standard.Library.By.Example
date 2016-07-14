"""Example use of popen() varients from os.

"""

# Ignore deprecation warnings
import warnings
warnings.filterwarnings('ignore', 'os.popen.* is deprecated.*',)

import os

print 'popen2:'
stdin, stdout = os.popen2('cat -')
try:
    stdin.write('through stdin to stdout')
finally:
    stdin.close()
try:
    stdout_value = stdout.read()
finally:
    stdout.close()
print '\tpass through:', repr(stdout_value)
