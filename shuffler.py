#!/usr/bin/python
# -*- coding: utf-8 -*-

# This is the function for shuffling
from random import shuffle as shuffleFunction

def __shuffledCards(num):
    '''
    Return a shuffled list from range of 0 to num.
    num: number of cards
    '''
    tempList = list(range(0, num))
    shuffleFunction(tempList)
    return tempList
