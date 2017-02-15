#!/usr/bin/python
from __future__ import print_function
import random, string
myrg = random.SystemRandom()
# If you want non-English characters, remove the [0:52]
f = open('l789.txt','w')
alphabet = string.letters[0:52] + string.digits
for x in range(100,200):
 pw = str().join(myrg.choice(alphabet) for _ in xrange(7))
 print(pw,file=f)
 pw = str().join(myrg.choice(alphabet) for _ in xrange(8))
 print(pw,file=f)
 pw = str().join(myrg.choice(alphabet) for _ in xrange(9))
 print(pw,file=f)
