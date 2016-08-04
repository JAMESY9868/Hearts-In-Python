#!/usr/bin/python
# -*- encoding: utf-8 -*-

# series number = 13 * m + n
# m: 0->Spades, 1->Hearts, 2->Clubs, 3->Diamonds
# n: 0~7->2~9, 8->10, 9~12->JQKA

from platform import system # system determines whether the program is run on a Windows, a Mac of a Linux computer.
from color import color # to make use of the colors

class card:
    'Represents a digital version of a poker card'
    _series = -1 # Initialize it by -1
    _suites = ('♠♥♣♦', 'SHCD')
    # _numbers = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')
    _numbers = tuple([' ' * (2 - len(number)) + number for number in \
        ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')])
    def setMN(self, m, n):
        'Sets the m, n values and return self'
        self._series = 13 * m + n
        return self
    def getMN(self):
        'Gets the m, n values'
        return (lambda x, n: (x // n, x % n))(self._series, 13)
    def setSeries(self, series = -1):
        'Sets the series number and return self'
        # This method is only supposed to be used in initializing a deck of cards
        self._series = -1 if series < 0 else series
        return self
    def getSeries(self):
        'Gets the series number'
        return self._series
    def str(self, colored = True):
        'Displays the card as text'
        sysName = system()
        mnToStr = lambda mnTuple, indexOfSuites: \
            'Undefined card' if mnTuple[0] < 0 or mnTuple[1] < 0 else \
            card._suites[indexOfSuites][mnTuple[0]] + card._numbers[mnTuple[1]]
        #####################################################################################
        # the current decision is that if windows, output SHCD and otherwise output unicode #
        #####################################################################################
        return ((color() if self.getMN()[0] %2 == 0 else color('red')).text \
            if colored else (lambda x: x))(mnToStr(self.getMN(), 'Windows' == sysName))
    def print(self, colored = True):
        print(self.str(colored))
    ################################
    # The section for game playing #
    ################################
    def compare(self, currGreat):
        '''compare whether it is the greater card according to the current suite
        returns true if it is, false otherwise'''
        return False if self.getMN()[0] != currGreat.getMN()[0] else \
            self.getMN()[1] > currGreat.getMN()[1]
    def sortKey(self):
        '''When sorting hand, sort by the order:
            suites as Clubs-Diamonds-Spades-Hearts
            number from lowest to greatest
            
            The easiest way to do this is to add 
            +series numbers of Spades and Hearts by 4 * 13
        '''
        return self._series + (0 if self.getMN()[0] > 1 else 52) 

        
pass
