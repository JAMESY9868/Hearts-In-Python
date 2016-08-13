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
    print(playedCards)
def handOutCards(handOfCards, overAllScore, targetPlayerNum):
    if targetPlayerNum==0：
        return []
    else:
        playerPrintLine("Please type in the indices of the cards counted from left to right (starting from 0) that you would like to hand out to"+ targetPlayerNum + ".(please type in the numbers in this way: 1 2 3)")
        string=input.split()
        exchangeCards=[]
        for i in string:
            exchangeCards+=handOfCards[i]
        return exchangeCards



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

def playCards(handOfCards, othersCards, overAllScore):
    'the human action for playing out cards'
    ####################################################################
    # First, print what others have played out, USING playedCardsPrint
    # third, print the informational line:
    #    'Please type in the index of the card counted from left to right (starting from 0) that you would like to play.'
    # last, print the current hand ___USING playerPrintLine___
    # and asks for the input
    #
    # returns a card object to play out
    ####################################################################
