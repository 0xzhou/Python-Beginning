# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 13:54:41 2019

@author: Dell
"""


import numpy as np
A=np.arange(12).reshape((3,4))
print(A)
print(np.split(A,2,axis=1)) # axis=1,对列进行操作，分割成两块
print(np.split(A,3,axis=0)) # axis=0,对行进行操作，分割成三块

print(np.array_split(A,3,axis=1)) # 不等分割，how to set the number in a block?

print(np.vsplit(A,3)) #纵向分割
print(np.hsplit(A,2)) #横向分割

