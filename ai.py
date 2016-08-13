#!/usr/bin/python
# -*- encoding: utf-8 -*-

from hand import hand
from card import card

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
    if not targetPlayerNum: return [] # if 0, do nothing
    allHearts = [cardValues[c.getMN()] for c in handOfCards]
    ifShootMoon = (0, 10) in handOfCards and \
        5 <= len([x for x in allHearts if x > 0]) \
        and 2 >= len([x for x in allHearts if x < 0])
    return sorted(
        sorted(handOfCards[:], \
            key = lambda crd: cardValues[crd.getMN()], \
            reverse = not ifShootMoon)[:3] # returns three cards
        , key = card.sortKey
    )

def playCards(handOfCards, othersCards, overAllScore):
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
    
    