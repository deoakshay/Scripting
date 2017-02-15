#!/usr/bin/python
from __future__ import print_function
import random, string
myrg = random.SystemRandom()
length = 9
# If you want non-English characters, remove the [0:52]
f = open('l9.txt','w')
alphabet = string.letters[0:52] + string.digits
for x in range(100,200):
 pw = str().join(myrg.choice(alphabet) for _ in xrange(length))
 print(pw,file=f)
