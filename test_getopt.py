#!/usr/bin/env python

import getopt
import sys

options, args=getopt.gnu_getopt(sys.argv, 'nl', ['n='])

print [int(i) if i.isdigit() else 0 for i in zip(*options)[1]]

