#!/usr/bin/env python
#mapper.py

import string
import sys

adj_list = []

for line in sys.stdin:
    line = line.strip()
    line = line.lower()
    words = line.split()



    for word in words:
        for c in string.punctuation:
            word = word.replace(c, "")

        # print each word by itself
        print'%s,$\t%s' % (word, len(words)-1)

        for next_word in words: #[words.index(word)+1:]:
            if next_word != word:
                print'%s,%s\t%s' % (word, next_word, 1)
                # print'%s,%s\t%s' % (next_word, word, 1)

