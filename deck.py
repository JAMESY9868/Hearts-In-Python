#!/usr/bin/python
# -*- coding: utf-8 -*-

from random import shuffle # imports the function shuffle
from card import card # imports the class card

class deck:
    'Represents a deck of cards.'
    numOfCards = 52 # number of cards WITHOUT JOKERS
    cards = list(range(0, numOfCards)) # a list of cards numbered from 0 to 51
    cards = [card().setSeries(i) for i in range(0, numOfCards)] # a list of cards numbered from 0 to 51
    def shuffle(self):
        'The shuffling is basically to shuffle the "cards" member (which is a list)'
        shuffle(self.cards)
    def __init__(self, ifShuffled = True):
        '''
        The constructor of the class
        
        sets cards as 
        '''
        self.cards = self.__shuffledCards