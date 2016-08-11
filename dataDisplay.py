#!/usr/bin/python
# -*- encoding: utf-8 -*-

from shutil import get_terminal_size as terminalSize # the size of the terminal window

def display(players):
    termSize = terminalSize()
    if termSize[0] < 60 or termSize[1] < 10:
        print('Terminal size too small. Please enlarge your terminal window to proceed.' + \
            '\nCurrent terminal Size: columns={}, lines={}' % tuple(termSize))
        raise ValueError
def _debugTerminalSizeDisplay():
    print('Columns: %d, lines: %d' % tuple(terminalSize()))

def playerPrintLine(printData):
    'I will change this later'
    print(printData)