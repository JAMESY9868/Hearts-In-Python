#!/usr/bin/python
# -*- encoding: utf-8 -*-

import pdb # debugging module

_ifDebug = True
_debugAllAI = True
trace = pdb.set_trace if _ifDebug else lambda: None