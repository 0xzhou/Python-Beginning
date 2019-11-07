'''
 tile() creates a new array by repeating an input array
 np.tile(A = , reps = )
 A--input array
 reps=number of repeat times, also structure of the tiled output

 np.tile(A = , reps = [row-repeats, col-repeats] )
'''

import numpy as np

# 1d examples
A=[6,7,8]
B=np.tile(A, reps=2) #copy the A for 2 times horizontally
print(B)
C=np.tile(A, reps=(2,1)) #vertically
print(C)
D=np.tile(A, reps=(3,2))
print(D)

# 2d examples
A2=[[6,7], [8,9]]
B2=np.tile(A2, reps=[2,2])
print(B2)

C2=np.tile(A2,reps=[2,2,2])
print(C2)