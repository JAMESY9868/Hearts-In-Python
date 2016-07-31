#!/usr/bin/python
# -*- coding: utf-8 -*-

class deck:
    '''
    Represents a deck of cards.
    '''
    numOfCards = 52 # number of cards WITHOUT JOKERS
    cards = list(range(0, numOfCards))
        # 
    
    @staticmethod # this function is static, meaning it does not depend on deck
    def __shuffledCards(cards):
        '''
        Return a shuffled list from range of 0 to num.
        num: number of cards
        '''
        

        tempList = list(range(0, num))
        shuffleFunction(tempList)
        return tempList

    def __init__(self):
        '''
        The constructor of the class
        
        sets cards as 
        '''
        self.cards = self.__shuffledCards