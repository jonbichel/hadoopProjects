#!/usr/bin/env python
#mapper.py

import string
import sys

for line in sys.stdin:
    line = line.strip()
    row, column, value = line.split(',')

    """
    for word in words:
        for c in string.punctuation:
            word=word.replace(c,"")
     """

    print'%s,%s,%s' % (column,row,value)
