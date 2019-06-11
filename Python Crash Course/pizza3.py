# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 22:31:52 2019

@author: Dell
"""

def make_pizza(size, *toppings):
    print("\nMaking a "+str(size)+"-inch pizza with the following toppings:") # the str() 显式的指出将int size输出为字符串
    for topping in toppings:
        print(topping)
        
make_pizza(16,"BBQ","steaks")
make_pizza(18,"green onion","sausage")