#!/usr/bin/env python
#-*- coding: utf-8 -*-

"""
__version__ =   "0.1"
__author__  =   "@lantip"
__date__    =   "2013/06/15"

an extend from RoygBiv
"""

from roygbiv import *
import sys
import json

def analize(images):
	t = Roygbiv(images)
	result = []
	rgbs = tuple(t.get_palette_rgb())
	hexs = t.get_palette_hex()
	result.append({"rgb": rgbs})
	result.append({"hex": hexs})
	return json.dumps(result)


if __name__ == '__main__':
	question = raw_input('> ')
	while (question != 'quit'):
		try:
			t = analize(question)
			print t
			question = raw_input('> ')
		except:
			sys.exit(1)
