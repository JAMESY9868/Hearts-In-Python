#!/usr/bin/python
# -*- encoding: utf-8 -*-

from deck import deck # a deck of cards
from hand import hand # unsure if necessary, as not being explicitly used
from player import player, playerNames

from debugMode import pdb, _ifDebug, _debugAllAI, trace # debug tools

def main():
    players=[player() for i in range(4)]
    players[0].setMode(not _debugAllAI)
    for i in range(0,4):
        players[i].setAllPlayers(players)
        players[i].setPlayerNum(i)
    overAllScore = [0, 0, 0, 0]
    playedRounds = 0
    while True not in [i > 99 for i in overAllScore]: # each game is a loop
        playedRounds += 1
        [each[0].getHand(each[1]) for each in zip(players, deck().fourHands())]
        handOutTurn(players, overAllScore, playedRounds)
        playTurn(players, overAllScore, playedRounds)
        print()
        trace()
    print('You get ' + 
        ['first', 'second', 'third', 'last']
            [[i for i in range(4) if sorted(overAllScore)[i] == overAllScore[0]][0]] +
        'place.')
def handOutTurn(players, overAllScore, playedRounds):
    if _ifDebug: players[0].handOfCards.printData()
    lst=[[] for i in range(4)]
    numHanding = lambda i, ifToGive = True: (i + 
        [-1, 1][ifToGive] * [1, 3, 2, 0][(playedRounds - 1) % 4]) % 4
    trace()
    for i in range(4):
        lst[i] += players[i].handOutCards(overAllScore, [1, 3, 2, 0][(playedRounds - 1) % 4])
    trace()
    for i in range(4):
        if len(lst[i]): # if there are any cards, get rid of the cards
            for crd in lst[i]:
                players[i].handOfCards.playCardByCard(crd)
            # the # of the other player who hands card to the curr player
            for crd in lst[i]:
                players[numHanding(i)].handOfCards.obtainCards(crd)
    if _ifDebug: players[0].handOfCards.printData()
    print('You handed out ' + ' '.join([crd.str() for crd in lst[0]]))
    print('You received ' + ' '.join([crd.str() for crd in lst[numHanding(0, False)]]))
def playTurn(players, overAllScore, playedRounds):
    if _ifDebug: [plyr.handOfCards.printData() for plyr in players]
    currScore = [0 for i in range(4)]
    lastTurnHighest = [i for i in range(4) if (2, 0) in players[i].handOfCards][0]
    canHearts = False
    for i in range(13):
        print('Starting with ' + (('you',) + playerNames)[lastTurnHighest] + '.')
        othersCards = []
        high = None
        for j in range(4):
            currPlayer = (j + lastTurnHighest) % 4
            othersCards.append(players[currPlayer].playCards(othersCards, overAllScore, canHearts))
            players[currPlayer].handOfCards.playCardByCard(othersCards[-1])
            high = othersCards[-1].higher(high)
        lastTurnHighest += [i for i in range(4) if high == othersCards[i]][0]
        lastTurnHighest %= 4
        scores = sum([crd.score() for crd in othersCards])
        currScore[lastTurnHighest] += scores
        overAllScore[lastTurnHighest] += scores
        if not canHearts and scores % 13: canHearts = True # if someone plays hearts, the score shouldn't be multiple of 13
        if i - 12:
            print('Scores for current game: ' + 
                ' | '.join([': '.join(parts) for parts in zip(('You',) + playerNames, 
                    [str(i) for i in currScore])]))
            print('Overall score: ' + ' | '.join([': '.join(parts) for parts in zip(('You',) + playerNames, 
                [str(i) for i in overAllScore])]))
    if 26 == max(currScore):
        trace()
        currScore = [26 - i for i in currScore]
        for i in range(4): overAllScore[i] += currScore[i] # if shoot moon, every one else gets points instead
    print('Scores for current game: ' + 
        ' | '.join([': '.join(parts) for parts in zip(('You',) + playerNames, 
            [str(i) for i in currScore])]))
    print('Overall score: ' + ' | '.join([': '.join(parts) for parts in zip(('You',) + playerNames, 
        [str(i) for i in overAllScore])]))
    print()
    trace()

if __name__ == '__main__': main()
