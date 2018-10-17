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
        if len(word) <= 4:
            print'%s.%s\t%s' % (word, "a", 1)
        else:
            print'%s.%s\t%s' % (word[0:4], word[4:], 1)