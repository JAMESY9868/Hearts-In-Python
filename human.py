#!/usr/bin/python
# -*- encoding: utf-8 -*-

import hand

def handOutCards(handOfCards):
    'the human action for handing out cards'
    print('Please type in the indecs of the cards '
        + '\(from left to right, starting from 0\) ' +
        'you would like to ')
    print('Cards: ' + handOfCards)

def playCards(handOfCards, othersCards = []):
    'the human action for playing out cards'

