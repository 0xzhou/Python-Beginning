# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 22:33:40 2019

@author: Dell
"""

try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")