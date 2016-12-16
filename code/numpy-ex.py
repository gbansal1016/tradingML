# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 23:29:59 2016

@author: gbans6
"""

##%
import numpy as np
import time as time

print(np.ones(4,dtype=int))
print(np.random.normal(size=(2,3)))
print(np.random.randint(0,20,size=(2,3)))

a=time.time()
a = np.array([9, 6, 2, 3, 12, 14, 7, 10], dtype=np.int32)
print(a)
b=time.time()

index = np.where(a==14) 
print(index[0])
##%