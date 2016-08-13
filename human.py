#!/usr/bin/python
# -*- encoding: utf-8 -*-

import hand
import dataDisplay # use this module to implement playerPrintLine and playedCardsPrint
#from player import playerNames as names
playerNames = ('Ann', 'Bob', 'Dan')

names = playerNames

def playerPrintLine(printData):
    'PLEASE USE THIS. I WILL UPDATE THE FUNCTION IN THE OTHER FILE LATER'
    # print in the lower section
    dataDisplay.screenDataDump(2, printData)
def scorePrint(scoreData):
    'Dont USE THIS'
    # print(scoreData)
def playedCardsPrint(playedCards):
    'PLEASE IMPLEMENT AND USE THIS.'
    # print in the middle section
    dataDisplay.screenDataDump(1, playedCards)
def playerInput(prompt):
    return input(prompt)
def handOutCards(handOfCards, overAllScore, targetPlayerNum):
    if targetPlayerNum==0:
        return []
    else:
        playerPrintLine('Please type in the indices of the cards counted from left to right (starting from 0) that you would like to hand out to ' + ['Ann', 'Bob', 'Dan'][targetPlayerNum] + '. (please type in the numbers in this way: 1 2 3)')
        
        result = ''
        while result == '':
            result = playerInput('Please type in the indices: ')
            try:
                result = [handOfCards[int(i)] for i in result.split()]
                if len(result) != 3: 1 / 0
                return result
            except: result = ''
        



    ####################################################################
    # First, print the informational line:
    #    'Please type in the indices of the cards counted from left to right (starting from 0) that you would like to hand out to ' + TARGETNAME + '.'
    # last, print the current hand ___USING playerPrintLine___
    # and asks for the input
    #
    # returns a list of cards (3 cards) to hand out to the player
    ####################################################################
    # NOTE: If the target player number is 0 (the player himself), do nothing
    ####################################################################

def playCards(handOfCards, othersCards, overAllScore, ifShootMoon = False, canHearts = False):
    'the human action for playing out cards'
    # othersCards: a list of 0~3 cards
    ####################################################################
    # First, print what others have played out, USING playedCardsPrint 'SQ HQ CQ'
    # third, print the informational line:
    #    'Please type in the index of the card counted from left to right (starting from 0) that you would like to play.'
    # last, print the current hand ___USING playerPrintLine___
    # and asks for the input using playerInput
    #
    # returns a card object to play out
    ####################################################################
    s = ''
    for crd in othersCards:
        s += crd.str() + ' '
    playedCardsPrint(s[:-1])
    playerPrintLine("Please type in the index of the card counted from left to right (starting from 0) that you would like to play.")
    playerPrintLine(handOfCards.str())
    result = ''
    while result == '':
        result = playerInput("Please type in the input")
        try:
            result = int(result)
            if (not canHearts and 1 == handOfCards[result]) or (not len(othersCards) and othersCards[0].getMN()[0] != handOfCards[result].getMN()[0] and (othersCards[0].getMN()[0] in [crd.getMN()[0] for crd in handOfCards])): raise ValueError
            return handOfCards[result]
        except:
            result = ''
