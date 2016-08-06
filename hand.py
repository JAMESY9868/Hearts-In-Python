#!/usr/bin/python
# -*- encoding: utf-8 -*-

from card import card

class hand:
    def __init__(self, cards = []):
        'Initialize cards'
        self.cards = sorted(cards, key = card.sortKey) # Clb-Dmnd-Spd-Hrt
    def playCardByIndex(self, index):
        temp = self.cards[index]
        del self.cards[index]
        return temp
    def playCardByCard(self, card):
        for i in range(len(self.cards)):
            if self.cards[i] == card: return self.playCardByInd(i)
    def giveThreeCards(self, indeces, target):
        'Give three cards out to target'
        if len(indeces) - 3: raise ValueError # if length != 3, error
        given = [self.cards[i] for i in indeces]
        for i in indeces: del self.cards[i]
        target.obtainCards(given)
    def obtainCards(self, cards):
        'Obtain cards'
        self.cards += cards
        self.cards = sorted(self.cards, key = card.sortKey)


pass
