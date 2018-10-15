#!/usr/bin/env python
#mapper.py

import string
import sys
import fileinput

#nameOfFile = os.getenv("input_file_name")

for line in sys.stdin:
    line = line.strip()
    line = line.lower()
    words = line.split()

    nameOfFile = fileinput.filename()

    for word in words:
        for c in string.punctuation:
            word = word.replace(c,"")

        print'%s\t%s' % (word, nameOfFile)
