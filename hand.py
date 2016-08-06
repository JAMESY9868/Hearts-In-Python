#!/usr/bin/python
# -*- encoding: utf-8 -*-

from card import card

class hand:
    def __init__(self, cards = []):
        'Initialize cards'
        self.__cards = sorted(cards, key = card.sortKey) # Clb-Dmnd-Spd-Hrt
    def playCardByIndex(self, index):
        temp = self.__cards[index]
        del self.__cards[index]
        return temp
    def playCardByCard(self, card):
        for i in range(len(self.__cards)):
            if self.__cards[i] == card: return self.playCardByInd(i)
    def giveThreeCards(self, indeces, target):
        'Give three cards out to target'
        if len(indeces) - 3: raise ValueError # if length != 3, error
        given = [self.__cards[i] for i in indeces]
        for i in indeces: del self.__cards[i]
        target.obtainCards(given)
    def obtainCards(self, cards):
        'Obtain cards'
        self.__cards += cards
        self.__cards = sorted(self.__cards, key = card.sortKey)
    #############################################################################################
    ################################ METHODS FOR DEBUGGING ONLY #################################
    #############################################################################################
    @staticmethod
    def __debug_init(cardsSeries = []):
        'FOR DEBUG ONLY. Takes in 13 series numbers of cards'
        if type(cardsSeries) != list or len(cardsSeries) > 51: raise ValueError
        return hand([card().setSeries(n) for n in cardsSeries])

pass
