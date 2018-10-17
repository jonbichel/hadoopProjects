#!/usr/bin/env python
#mapper.py

import string
import sys

for line in sys.stdin:
    line = line.strip()
    line = line.lower()
    words = line.split()

    for word in words:
        for c in string.punctuation:
            word = word.replace(c,"")

    for word in words:
        if word.length() <= 4:
            print'%s.%s' % (word, "" )
        else:
            print'%s.%s' % (word[0:4], word[4:])