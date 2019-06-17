# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 14:06:38 2019

@author: Dell
"""

import numpy as np
a=np.arange(4)
print(a)

# 完全复制并关联a:
b=a #完全复制，类似指针？
print(b is a)
c=a
d=b
a[0]=99
print(a,b,c,d)

d[1]=88
print(a,b,c,d) # 四个变量指向的内容全部改变

# deep copy:只复制值，并不关联
b=a.copy() # deep copy
print(a,b)
a[2]=77
print(a,b)

