#!/usr/bin/env python
#mapper.py

import string
import sys

for line in sys.stdin:
    line = line.strip()
    line = line.lower()
    words = line.split()

    # used to keep track of previous word first iteration previous word is unknown
    prevWord = ""

    for word in words:
        for c in string.punctuation:
            word = word.replace(c,"")

        #
        print'%s\t%s\t%s' % (prevWord, word, 1)

        # keep track of previous word
        prevWord = word

# print last word
print'%s\t%s\t%s' % (prevWord, "", 1)