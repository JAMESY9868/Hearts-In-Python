#!/usr/bin/python
# -*- encoding: utf-8 -*-

from card import card

class hand:
    def __init__(self, cards):
        self.cards = sorted(cards, key = card.sortKey) # Clb-Dmnd-Spd-Hrt
    def playCards(self, index):
        temp = self.cards[index]
        del self.cards[index]
        return temp