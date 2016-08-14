#!/usr/bin/python
# -*- encoding: utf-8 -*-

from random import shuffle, seed, randrange # imports the function shuffle
from card import card # imports the class card
from hand import hand # imports the class hand

seed()

class deck:
    'Represents a deck of cards.'
    def shuffle(self):
        'The shuffling is basically to shuffle the "cards" member (which is a list)'
        shuffle(self.__cards)
    def __init__(self):
        'Initializes cards'
        # set self.__cards to be a list of cards serialized from 0 to 51
        self.__cards = [card().setSeries(i) for i in range(52)]
    def __giveCards(self, playerNum):
        'Returns a "hand", which contains a list of 13 cards'
        return hand(self.__cards[13 * playerNum : 13 * (playerNum + 1)])
    def fourHands(self, ifNeedShuffle = True):
        'Returns four hands after shuffling once'
        if ifNeedShuffle: [self.shuffle() for i in range(randrange(1, 0xff))]
        return [self.__giveCards(num) for num in range(4)]