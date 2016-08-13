#!/usr/bin/python
# -*- encoding: utf-8 -*-

from deck import deck # a deck of cards
from hand import hand # unsure if necessary, as not being explicitly used
from player import player

def main():
    players=[player(cards) for cards in deck().fourHands()]
    players[0].setMode(True)
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
    lst=[]
    for i in range(0,4):
        lst+=players[i].handOutCards(overAllScore, [1, 3, 2, 0][(playedRounds - 1) % 4])
    for i in range(0,4):
        if lst[0]: # get rid of the card
            for crd in lst[i]: players[i].handOfCards.playCardByCard(crd)
        for crd in lst[i]: players[(i - [1, 3, 2, 0][(playedRounds - 1) % 4]) % 4].handOfCards.obtainCards(crd)
def playTurn(players, overAllScore, playedRounds):
    for i in range(13):
        othersCards = []
        for j in range(4):
            othersCards += players[j].playCards(othersCards, overAllScore)
        high = othersCards[0]
        for k in range(3):
            high = othersCards[k] if othersCards[k].compare(high) else high
        scores = sum([crd.score() for crd in othersCards])
            





if __name__ == '__main__': main()
