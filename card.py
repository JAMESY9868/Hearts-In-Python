#!/usr/bin/python
# -*- encoding: utf-8 -*-

# series number = 13 * n + m
# n: 0~3, m: 0~12
#
# n: 0->Spades, 1->Hearts, 2->Clubs, 3->Diamonds
# m: 0~7->2~9, 8->10, 9~12->JQKA

class card:
    '''
    Represents a digital version of a poker card
    '''
    series = -1 # Initialize it by -1
    @staticmethod
    def series(n, m):
        '''
        n: 0~3 => SHCD
        m: 0~12 => 2~9, 10, JQKA
        '''
        return m + 13 * n

    def __init__(self):
        pass