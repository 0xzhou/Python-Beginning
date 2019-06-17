# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 16:37:27 2019

@author: Dell
"""

# create a graph
import numpy as nm
import tensorflow as tf
with tf.device('/gpu:2'):
    a=tf.constant([1.0,2.0,3.0,4.0,5.0,6.0],name='a')
    b=tf.constant([1.0,2.0,3.0,4.0,5.0,6.0],name='b')
    c=tf.multiply(a,b)
    print(c)