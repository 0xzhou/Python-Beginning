# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 22:38:26 2019

@author: Dell
"""

def build_profile(first,last,**user_info):
    """"创建一个字典，其中包含我们知道的有关用户的一切"""
    profile={}
    profile['first name']=first
    profile['laste name']=last
    for key, value in user_info.items(): # 遍历字典user_info, 并且把名称-值“对”添加到profile中
        profile[key]=value
    return profile

user_profile=build_profile('albert','einstein',location='princaton',field='physics')
print(user_profile)