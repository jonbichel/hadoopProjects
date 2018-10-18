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

        if word != '':
            if len(word) == 1:
                print'%s.%s\t%s' % (word[0], "", 1)
            else:
                print'%s.%s\t%s' % (word[0], word[1:], 1)


        """
        if len(word) <= 4:
            print'%s.%s\t%s' % (word, "", 1)
        else:
            print'%s.%s\t%s' % (word[0:4], word[4:], 1)
        """