#!/usr/bin/python
# -*- coding: utf-8 -*-

from os import system # system commands
from platform import system as platSys # OS name

def clc():
    'Clear the screen'
    system('cls' if 'Windows' == platSys() else 'clear')








def main():
    result = input('Please type in your name: ')






if __name__ == '__main__': main()
