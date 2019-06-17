# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 14:15:55 2019

@author: Dell
"""

import pandas as pd
import numpy as np

s=pd.Series([1,3,4,np.nan,44,1])
print(s)

dates=pd.date_range('20190617',periods=6)
print(dates)

df=pd.DataFrame(np.random.randn(6,4),index=dates,columns=['a','b','c','d']) # index->行，columns->列
print(df)

df1=pd.DataFrame(np.arange(12).reshape(3,4)) #default one
print(df1)

# df=pd.DataFrame({'A':1,'B':pd.Timestamp('20190617'),'C'})

print(df1.columns,df1.index)
print(df1.values)
print(df1.describe())

#dt.T # Transpose