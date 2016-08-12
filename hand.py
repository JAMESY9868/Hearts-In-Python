#!/usr/bin/python
# -*- encoding: utf-8 -*-

from card import card
from sys import stdout
from platform import system

def printf(format, *args): # to simulate C's printf function due to a weird bug in python's print
    stdout.write(format % args)

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
    def giveThreeCards(self, indices, target):
        'Give three cards out to target'
        if len(indices) - 3: raise ValueError # if length != 3, error
        given = [self.__cards[i] for i in indices]
        for i in indices: del self.__cards[i]
        target.obtainCards(given)
    def obtainCards(self, cards):
        'Obtain cards'
        self.__cards += [cards] if type(cards) == card else cards
        self.__cards = sorted(self.__cards, key = card.sortKey)
    def str(self, colored = True, multiline = False):
        'For Windows, "colored" is deprecated and set always to be False'
        colored &= system() != 'Windows'
        tempStr = ''
        for crd in self.__cards: tempStr += crd.str(colored) + \
            ('\n' if multiline else ' ')
        return tempStr[:-1] # to remove the last '\n' or space
    def print(self, colored = True, multiline = False):
        'For Windows, "colored" is deprecated and set always to be False'
        print(self.str(colored, multiline))
        # the code above somehow does not work, possibly a bug for ANSI escape sequences
        # for crd in self: printf('%s' + ('\n' if multiline else ' '), crd.str(colored))
        # printf('\n')
    #############################################################################################
    ######################################## OPERATORS ##########################################
    #############################################################################################
    def __contains__(self, item):
        return (item if type(item) == card else card().setSeries(item) 
            if type(item) == int else card().setMN(*item)) in self.__cards
    def __getitem__(self, index):
        return self.__cards[index]
    #############################################################################################
    ##################################### END OF OPERATORS ######################################
    #############################################################################################
    ################################ METHODS FOR DEBUGGING ONLY #################################
    #############################################################################################
    @staticmethod
    def __debug_init(cardsSeries = []):
        'FOR DEBUG ONLY. Takes in 13 series numbers of cards'
        if type(cardsSeries) != list or len(cardsSeries) > 52: raise ValueError
        return hand([card().setSeries(n) for n in cardsSeries])
pass
debug_only_hand = hand._hand__debug_init(list(range(52)))
