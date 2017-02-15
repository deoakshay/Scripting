#!/usr/bin/python
from __future__ import print_function
import random, string
import hashlib
# If you want non-English characters, remove the [0:52]
str= raw_input("File: ");
f = open(str,'r')
f1= open('sha.txt','a')
for line in f:
 hash_object = hashlib.sha256(line)
 hex_dig= hash_object.hexdigest()
 print(hex_dig,file=f1)
