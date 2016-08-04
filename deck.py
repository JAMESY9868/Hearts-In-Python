#!/usr/bin/python
# -*- coding: utf-8 -*-

from random import shuffle # imports the function shuffle
from card import card # imports the class card
from hand import hand # imports the class hand

class deck:
    'Represents a deck of cards.'
    def shuffle(self):
        'The shuffling is basically to shuffle the "cards" member (which is a list)'
        shuffle(self.cards)
    def __init__(self, ifShuffled = True):
        '''
        initializes cards 
        '''
        self.cards = \
            [card().setSeries(i) \
                for i in range(0, 52)] # a list of cards numbered from 0 to 51
    def giveCards(self, playerNum):
        'Returns a "hand", which contains a list of 13 cards'
        return hand(self.cards[13 * playerNum : 13 * (playerNum + 1)])