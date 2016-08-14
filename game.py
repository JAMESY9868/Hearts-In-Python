#!/usr/bin/python
# -*- encoding: utf-8 -*-

from deck import deck # a deck of cards
from hand import hand # unsure if necessary, as not being explicitly used
from player import player

_if_all_ai = True

def main():
    players=[player(cards) for cards in deck().fourHands()]
    players[0].setMode(not _if_all_ai)
    for i in range(0,4):
        players[i].setAllPlayers(players)
        players[i].setPlayerNum(i)
    overAllScore = [0, 0, 0, 0]
    playedRounds = 0
    while True not in [i > 99 for i in overAllScore]:
        playedRounds += 1
        handOutTurn(players, overAllScore, playedRounds)
        playTurn(players, overAllScore, playedRounds)
def handOutTurn(players, overAllScore, playedRounds):
    lst=[[] for i in range(4)]
    for i in range(4):
        lst[i] += players[i].handOutCards(overAllScore, [1, 3, 2, 0][(playedRounds - 1) % 4])
    playerNumHandingToHuman = -1
    for i in range(4):
        if lst[i][0]: # if there are any cards, get rid of the cards
            for crd in lst[i]:
                players[i].handOfCards.playCardByCard(crd)
            temp = (i - [1, 3, 2, 0][(playedRounds - 1) % 4]) % 4 # the # of the other player who hands card to the curr player
            if not temp: playerNumHandingToHuman = i
            for crd in lst[i]:
                players[playerNumHandingToHuman].handOfCards.obtainCards(crd)
    print('You handed out ' + ' '.join([crd.str() for crd in lst[0]]))
    print('You received ' + ' '.join([crd.str() for crd in lst[playerNumHandingToHuman]]))
def playTurn(players, overAllScore, playedRounds):
    lastTurnHighest = [i for i in range(4) if (2, 0) in players[i].handOfCards][0]
    canHearts = False
    for i in range(13):
        othersCards = []
        for j in range(4):
            currPlayer = (j + lastTurnHighest) % 4
            othersCards.append(players[currPlayer].playCards(othersCards, overAllScore, canHearts))
            players[currPlayer].handOfCards.playCardByCard(othersCards[-1])
        high = othersCards[0]
        for k in range(3):
            high = othersCards[k] if othersCards[k].compare(high) else high
        scores = sum([crd.score() for crd in othersCards])
        if not canHearts and scores % 13: canHearts = True # if someone plays hearts, the score shouldn't be multiple of 13

if __name__ == '__main__': main()
