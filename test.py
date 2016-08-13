#!/usr/bin/python
# -*- encoding: utf-8 -*-

import ai
import hand
import card
import human

def tester():
    'This tester uses the idea that T(F) is equiv to 1(0), and the fact that dividing by 0 is an error'
    result = 0
    rsltFunc = lambda testFunction, testInputLists, testResults: 1 / \
        (False not in unitTest(testFunction, testInputLists, testResults))
    # section: ai testing
    result += rsltFunc(
        ai.handOutCards, 
        [
            [hand.hand._hand__debug_init([11, 12, 19, 25, 26, 28, 38, 39, 40, 41, 42, 50, 51]), [], 1], 
            [hand.hand._hand__debug_init([11, 12, 19, 25, 26, 28, 38, 39, 40, 41, 42, 50, 51]), [], 0],
        ],
        [
            [card.card().setSeries(ser) for ser in [11, 12, 25]],
            [],
        ]
    )
    # section: card testing
    result += rsltFunc(
        card.card.score,
        [
            [card.card().setMN(2, 8)],
            [card.card().setMN(0,10)],
        ],
        [
            0,
            13,
        ]
    )

    # section: human testing
    result+=rsltFunc(
        human.handOutCards,
        [
           # [hand.hand._hand__debug_init([11, 12, 19, 25, 26, 28, 38, 39, 40, 41, 42, 50, 51]), [], 1], 
            [hand.hand._hand__debug_init([11, 12, 19, 25, 26, 28, 38, 39, 40, 41, 42, 50, 51]), [], 0],
        ],
        [
           # [card.card().setSeries(ser) for ser in [11, 12, 25]],
            [],
        ]
    )
def unitTest(testFunction, testInputLists, testResults):
    if len(testInputLists) != len(testResults): raise ValueError

    # the following line simulates snap's map using elements from multiple lists as input
    return [testFunction(*input) == result for input, result in zip(testInputLists, testResults)]


if __name__ == '__main__': tester()