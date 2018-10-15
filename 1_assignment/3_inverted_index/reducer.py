#!/usr/bin/env python
#reducer.py

import string
import sys

prev_key = None
fileNameSet = set()

for line in sys.stdin:
    line = line.rstrip()
    word,fileName = line.split('\t')
    if prev_key == None:  # is None
        prev_key = word
        fileNameSet.add(fileName)
        continue
    if prev_key == word:
        fileNameSet.add(fileName)
        continue
    if prev_key!=word:
        print '%s\t%s' %(prev_key, fileNameSet)
        prev_key=word
        fileNameSet.clear()
        fileNameSet.add(fileName)
print '%s\t%s' % (prev_key, fileNameSet)
