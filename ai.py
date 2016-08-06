#!/usr/bin/python
# -*- encoding: utf-8 -*-

from hand import hand

#####################################################################################################################################
#################################################### START OF handOutScores DATA ####################################################
#####################################################################################################################################
# the data down are experimental
handOutScores = {} # Spade Queen
for i in range(7): handOutScores[(0, i)] = -50 + 3 * i # spade 2 to 8 -- because there is a spade queen, scores in Spades are extreme
for i in range(7, 10): handOutScores[(0, i)] = -30 + 3 * i # spade 9 to J
handOutScores[(0, 10)] = 100 # spade queen
for i in range(11, 13): handOutScores[(0, i)] = 50 + 3 * i # spade K and A -- same reason it is extreme
for i in range(7): handOutScores[(1, i)] = -3 + i // 2 # heart 2 to 8
for i in range(7, 13): handOutScores[(1, i)] = i // 2 # heart 9 to A
for i in range(7): 
    for j in range(2, 4): handOutScores[(j, i)] = -12 + i - j # diamond and club, clubs are 1 score higher
for i in range(7, 13): 
    for j in range(2, 4): handOutScores[(j, i)] = -5 + i + 2 * j # diamond and club, clubs are 2 score lower
handOutScores[(2, 0)] = 5 # club 2 for starting off the game
#####################################################################################################################################
##################################################### END OF handOutScores DATA #####################################################
#####################################################################################################################################

def handOutCards(handOfCards, overAllScore = [0, 0, 0, 0]):
    'The ai algorithm for handing out cards, returns three "card" objects'
    # evaluate how many high heart cards there is and if there is SQ
    # if ther is not enough high cards, try to get rid of high cards by score
    # otherwise try to get rid of lowest cards
    

def playCards(handOfCards, othersCards = [], overAllScore = [0, 0, 0, 0]):
    'the ai algorithm for playing out cards'

