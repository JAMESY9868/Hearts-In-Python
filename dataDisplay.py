#!/usr/bin/python
# -*- encoding: utf-8 -*-

from shutil import get_terminal_size as terminalSize # the size of the terminal window

def _debugTerminalSizeDisplay():
    print('Columns: %d, lines: %d' % tuple(terminalSize()))

def screenDataDump(dataNum, dataStr):
    'PLEASE USE THIS'
    # Don't worry about implementing this function. 
    #################################################
    # if dataNum is:
    #   0, the players broad dataNum
    #   1, dumping to the middle section
    #   2, dumping to the lower section
    #################################################
    print(dataStr)