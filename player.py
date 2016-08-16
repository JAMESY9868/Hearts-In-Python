#!/usr/bin/python
# -*- encoding: utf-8 -*-

import ai # ai is the module for ai actions
import human # human is the module of human action

from hand import hand

from debugMode import _ifDebug

playerNames = ('Ann', 'Bob', 'Dan')

class player:
    'A player, either human player or an AI'
    def __init__(self, ifHumanPlayer = False):
        'handOfCards: a "hand" of cards; ifHumanPlayer: whether this player is human'
        self.handOfCards = hand()
        self.score = 0
        self.allPlayers=[]
        self.playerNum=-1
        self.setMode(ifHumanPlayer)
    def getHand(self, handOfCards):
        self.handOfCards = handOfCards
    def setMode(self, ifHumanPlayer = False):        
        self.actionModule = human if ifHumanPlayer else ai
    def setAllPlayers(self, allPlayers):
        self.allPlayers=allPlayers
    def setPlayerNum(self, playerNum):
        self.playerNum=playerNum
    def handOutCards(self, overAllScore, targetPlayerNum):
        return self.actionModule.handOutCards(self.handOfCards, overAllScore, targetPlayerNum)
    def playCards(self, othersCards, overAllScore, canHearts):
        playedCard = self.actionModule.playCards(self.handOfCards, othersCards, overAllScore, self.playerNum, False, canHearts)
        print((('You', ) + playerNames)[self.playerNum] + ' played ' + playedCard.str() + '.')
        if _ifDebug: print(self.playerNum)
        return playedCard