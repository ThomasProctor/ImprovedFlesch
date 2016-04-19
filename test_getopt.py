#!/usr/bin/env python

import getopt
import sys

pos_variable = ['n=']
pos_default='nl'

options, args=getopt.gnu_getopt(sys.argv, pos_default, pos_variable)

#print [int(i) if i.isdigit() else 0 for i in zip(*options)[1]]
print options
#print args

def process_options(optionl,n_def,pos_variable, pos_default):
	if len(optionl) > 0:
		for i in optionl:
			if i[0] in pos_variable:
				if i[1].isdigit():
					return int(i[1])
				else:
					return n_def
			elif i[0] in pos_default:
				return n_def
			else:
				return 0
	else:
		return 0

pos_defaultl=['-' + i for i in list(pos_default)]
pos_variablel=['--' + i[:-1] for i in pos_variable]

print process_options(options, 2, pos_variablel, pos_defaultl)


