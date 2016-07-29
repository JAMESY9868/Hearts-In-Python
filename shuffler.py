#!/usr/bin/python

# This is the function for shuffling
from random import shuffle as shuffleFunction

def __shuffle(num):
    tempList = list(range(0, num))
    shuffleFunction(tempList)
    return tempList

pass

class deck:
    'a deck'