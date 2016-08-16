#!/usr/bin/python
# -*- encoding: utf-8 -*-

import pdb # debugging module

_ifDebug = True
_debugAllAI = False


_ifDebug = False


trace = pdb.set_trace if _ifDebug else lambda: None