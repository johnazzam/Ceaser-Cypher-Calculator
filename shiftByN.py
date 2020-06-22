#_*_ coding: utf-8 _*_

import string
import collections

def shift(rotateString, numberToRotateBy):
    upper = collections.deque(string.ascii_uppercase)
    lower = collections.deque(string.ascii_lowercase)

    upper.rotate(numberToRotateBy)
    lower.rotate(numberToRotateBy)

    upper = ''.join(list(upper))
    lower = ''.join(list(lower))

    return rotateString.translate(str.maketrans(string.ascii_uppercase, upper)).translate(str.maketrans(string.ascii_lowercase, lower))

inputString = input('What is the string to be shift by?')

for i in range(len(string.ascii_uppercase)):
    print (i, " : ", shift(inputString, i))
