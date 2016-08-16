#!/usr/bin/python
# -*- encoding: utf-8 -*-

from hand import hand
from card import card
from time import sleep
import random

from debugMode import _ifDebug, trace

sleepTime = .01 if _ifDebug else 1

playerNames = ('Ann', 'Bob', 'Dan')

##########################################################################################################################
################################################ START OF cardValues DATA ################################################
##########################################################################################################################
# the data down are experimental
cardValues = {} # Spade Queen
for i in range(7): cardValues[(0, i)] = -50 + 3 * i # spade 2 to 8 -- because of spade queen, scores in Spades are extreme
for i in range(7, 10): cardValues[(0, i)] = -30 + 3 * i # spade 9 to J
cardValues[(0, 10)] = 100 # spade queen
for i in range(11, 13): cardValues[(0, i)] = 50 + 3 * i # spade K and A -- for the same reason it is extreme
for i in range(7): cardValues[(1, i)] = -7 + i # heart 2 to 8
for i in range(7, 13): cardValues[(1, i)] = 5 + i # heart 9 to A
for i in range(7): 
    for j in range(2, 4): cardValues[(j, i)] = -12 + i - j # diamond and club, clubs are 1 score higher
for i in range(7, 13): 
    for j in range(2, 4): cardValues[(j, i)] = -5 + i + 2 * j # diamond and club, clubs are 2 score lower
cardValues[(2, 0)] = 5 # club 2 for starting off the game
###########################################################################################################################
################################################# END OF cardValues DATA ##################################################
###########################################################################################################################

def handOutCards(handOfCards, overAllScore, targetPlayerNum):
    'The ai algorithm for handing out cards, returns three "card" objects'
    # evaluate how many high heart cards there is and if there is SQ and if there are few enough low heart cards
    # if ther is not enough high cards, try to get rid of high cards by score
    # otherwise try to get rid of lowest cards
    sleep(sleepTime)
    if not targetPlayerNum: return [] # if 0, do nothing
    allHearts = [cardValues[c.getMN()] for c in handOfCards]
    ifShootMoon = (0, 10) in handOfCards and \
        5 <= len([x for x in allHearts if x > 0]) \
        and 2 >= len([x for x in allHearts if x < 0])
    return sorted(
        sorted(handOfCards, \
            key = lambda crd: cardValues[crd.getMN()], \
            reverse = not ifShootMoon)[:3] # returns three cards
        , key = card.sortKey
    )

def playCards(handOfCards, othersCards, overAllScore, playerNum, ifShootMoon = False, ifCanHearts = False):
    'the ai algorithm for playing out cards'
    ##########################################################################################
    # try to play the lowest high cards
    # get rid of high cards as fast as possible, maybe taking some risks
    # get rid of hearts (and high spades) first
    # if other people play harmless cards, play highest
    # if inevitable gain of score, play highest
    # account for probability of upcoming people playing low cards, and decide
    #+ whether play low or high cards (the risk-taking part)
    ##########################################################################################
    # try not to finish a suite
    # determine if possible (whether hand is high enouth, & whether someone else got scores)
    # save 1/2 high cards for each suite for score-gaining
    # for scoreless turns play lowest card
    # if negative-value cards' amount reduces to 5, start to play highest cards
    ##########################################################################################
    sleep(sleepTime)
    if _ifDebug: print(handOfCards.str() + ' ' + str(len(handOfCards)))
    othersHighest = lambda othersCards = othersCards: card() if not len(othersCards) else \
        sorted([crd for crd in othersCards], key = card.sortKey)[-1]
    sameSuite = lambda handOfCards = handOfCards, othersCards = othersCards: \
        [crd for crd in handOfCards if crd.getMN()[0] == 
            (othersCards[0] if len(othersCards) else card()).getMN()[0]]
    lessThanOthers = lambda handOfCards = handOfCards, ifRisking = False: \
        [crd for crd in sameSuite(handOfCards) if crd.getMN()[1] <= \
            othersHighest(othersCards).getMN()[1] + (3 if ifRisking else 0)]
    handAfterHearts = lambda handOfCards: \
        [crd for crd in handOfCards if ifCanHearts or crd.getMN()[0] != 1]
    limitHandWithHearts = lambda handOfCards, removeOrKeepOnly: \
        [crd for crd in handOfCards if removeOrKeepOnly ^ (crd.getMN()[0] == 1)]
    if len(handOfCards) == 13 and (2, 0) in handOfCards: return card().setMN(2, 0)
    canPlay = sameSuite()
    if not len(canPlay):
        if len(othersCards) or ifCanHearts: canPlay = handOfCards
        else: canPlay = limitHandWithHearts(handOfCards, True)
    if ifShootMoon: # returns the highest scored card
        return sorted(canPlay, key = lambda crd: cardValues[crd.getMN()])[-1]
    else:
        if not len(othersCards) and len(canPlay):
            return sorted(canPlay, key = lambda crd: cardValues[crd.getMN()])[0]
        # output the highest of card that avoids score gaining if possible
        elif len([c for c in sameSuite(canPlay) if c.getMN() != (0, 10)]) and 3 == len(othersCards) and \
            not sum([crd.score() for crd in othersCards]):
            return [c for c in sameSuite(canPlay) if c.getMN() != (0, 10)][-1] # if safe, play highest
        elif len(lessThanOthers(canPlay)): return lessThanOthers(canPlay)[-1]
        elif len(lessThanOthers(canPlay, True)): # if has cards that greater by 3, play the lowest of these (risking)
            return lessThanOthers(canPlay, True)[0]
        elif len(sameSuite(canPlay)): return sameSuite(canPlay)[-1] # if any same suite, return highest
        try:
            if [i for i in range(4) if overAllScore[i] == min(overAllScore)][0] == \
                ([i for i in range(len(othersCards)) if othersHighest() == othersCards[i]][0]
                    + playerNum - len(othersCards)) % 4: # go for the lowest score player
                return sorted(limitHandWithHearts(canPlay, True), key = lambda crd: cardValues[crd.getMN()])[-1]
            else: return sorted(limitHandWithHearts(canPlay, False),
                key = lambda crd: cardValues[crd.getMN()])[-1]
        except IndexError:
            try: return sorted(canPlay, key = lambda crd: cardValues[crd.getMN()])[-1]
            except: return sorted(handOfCards, key = lambda crd: cardValues[crd.getMN()])[-1]