# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 22:25:37 2019

@author: Dell
"""
def make_pizza(*toppings):
    """ print all the stuffs guest ordered using for-loop"""
    print("\nMaking a pizza with following toppings:")
    for topping in toppings:
        print('- '+ topping) # + 直接用于连接字符串
        
make_pizza("pepperoni")
make_pizza("chesse","green onion","mushrooms")
