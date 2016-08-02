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
    def str(self, colored = False):
        'Displays the card as text'
        sysName = system()
        mnToStr = lambda mnTuple, indexOfSuites: \
            'Undefined card' if mnTuple[0] < 0 or mnTuple[1] < 0 else \
            card._suites[indexOfSuites][mnTuple[0]] + card._numbers[mnTuple[1]]
        #####################################################################################
        # the current decision is that if windows, output SHCD and otherwise output unicode #
        #####################################################################################
        return \
            (color() if self.getMN()[0] %2 == 1 else color('red'))\
            .text(mnToStr(self.getMN(), 'Windows' == sysName))


pass
