#!/usr/bin/python
# -*- encoding: utf-8 -*-

import ai # ai is the module for ai actions
import human # human is the module of human action

playerNames = ('Ann', 'Bob', 'Dan')

class player:
    'A player, either human player or an AI'
    def __init__(self, handOfCards, ifHumanPlayer = False):
        'handOfCards: a "hand" of cards; ifHumanPlayer: whether this player is human'
        self.handOfCards = handOfCards
        self.actionModule = human if ifHumanPlayer else ai
    def handOutCards(self, overAllScore, targetPlayerNum):
        handedCards = self.actionModule.handOutCards(self.handOfCards, overAllScore, targetPlayerNum)
    def playCards(self, othersCards, overAllScore):
        playedCard = self.actionModule.playCards(self.handOfCards, othersCards, overAllScore)