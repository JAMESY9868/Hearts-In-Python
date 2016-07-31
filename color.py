#!/usr/bin/python
# -*- encoding: utf-8 -*-

class color:
    'ANSI Color Escapes'
    _colorDict = {
        'black': 30
        , 'red': 31
        , 'green': 32
        , 'yellow': 33
        , 'blue': 34
        , 'magenta': 35
        , 'cyan': 36
        , 'white': 37
    }
    _escapeHeadTail = ['\x1b[', 'm'] # this shouldn't be changed
    _escapeMid = ['0'] # a list of 1/2 elements of stringified numbers
    def __init__(self, foreground = None, background = None, intenseFore = False, intenseBack = False):
        '''
        Initializes with the attributes of: foreground, background, intenseFore, intenseBack
        foreground and background should be texts within such:
            ['black', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']
        '''
        # if both foreground and background are unset, escape to 'normal text'
        if foreground is None and background is None: return
        # if foreground or background is not set, set them to default values
        foreground, background = \
            'black' if foreground is None else foreground, \
            'white' if background is None else background
        # set numbers for foreground and background colors
        foreNum, backNum = color._colorDict[foreground], 10 + color._colorDict[background]
        # if intenseFore or intenseBack is True, then add foreNum or backNum by 60 (for color intensification).
        foreNum, backNum = \
            foreNum + 60 if intenseFore else foreNum, \
            backNum + 60 if intenseBack else backNum
        # put stringified data in to object
        self._escapeMid = [str(num) for num in (foreNum, backNum)]
    def str(self):
        'Output the text form of the ANSI color sequence'
        combine = lambda escapeHeadTail, escapeMid: \
            escapeHeadTail[0] + ';'.join(escapeMid) + escapeHeadTail[1]
        try: return combine(self._escapeHeadTail, self._escapeMid)
        except KeyError: return combine(self._escapeHeadTail, [0])
    def text(self, text):
        'To be used directly in print(), to output some colored text "text"'
        try: return self.str() + text + color().str()
        except TypeError: return '' # return nothing if it gets TypeError
pass
