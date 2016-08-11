#!/usr/bin/python
# -*- encoding: utf-8 -*-

import os
from platform import system as osName 

def clc(): os.system('cls' if 'Windows' == osName() else 'clear')