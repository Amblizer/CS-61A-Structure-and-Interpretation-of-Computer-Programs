#!/usr/bin/env python

'''One line palindrome in the video'''

text  = open('week1-02-en.txt', 'r').read().split()
words = set(text)   # class set obliviates all duplicates

{w for w in words if w==w[::-1] and len(w)==6}