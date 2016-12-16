# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 01:37:27 2016

@author: gbans6
"""

import sys

filename=sys.argv[1]

infile = open(filename)

for line in infile:
    print(line)
    
infile.close()
