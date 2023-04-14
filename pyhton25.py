#!/usr/bin/python3
import string
stmt="Hey ,where are you ?"
for c in stmt:
     if c in string.punctuation:
         print(c)