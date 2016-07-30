#!/usr/bin/python
# -*- encoding: utf-8 -*-

_dict = {
    0x0C: 13,
    0x10: 1,
    0x11: 1,
    0x12: 1,
    0x13: 1,
    0x14: 1,
    0x15: 1,
    0x16: 1,
    0x17: 1,
    0x18: 1,
    0x19: 1,
    0x1A: 1,
    0x1B: 1,
    0x1C: 1
}

def scoreOfCard(hexadecim):
    '''
    Takes in the hexadecimal format (by preficing 0x to the digits, for example 0x1A, without quotation marks), a two-digit number, of a card.
    The first digit should be 0~3, where 0 can be omitted, with 0 be spades, 1 hearts, 2 clubs, 3 diomands;
    The second digit should be 0~D, with 0 be KING, 1 be ACE, 2~9 be 2~9, A be 10, B be JACK, C be QUEEN.
    '''
    pass