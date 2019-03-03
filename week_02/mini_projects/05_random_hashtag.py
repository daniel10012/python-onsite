'''
--------------------------------------------------------
                RANDOM HASHTAG GENERATOR
--------------------------------------------------------

Programmatically generate random hashtags by picking from a word list.

Tip: In UNIX systems you can access a dictionary file at this path:
        /usr/share/dict/words

'''

import random

w = open("/usr/share/dict/words", "r")

#print(w.read())


list_words = []
for i in w:
    list_words.append(i.strip("\n"))



for i in range(0,10):
    r = random.randint(1, len(list_words))
    print("#" + list_words[r])