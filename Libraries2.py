import sys

from Libraries import greet, farewell

if len(sys.argv) == 2:
    greet(sys.argv[1])
