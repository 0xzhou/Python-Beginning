import numpy as np

A=np.array([1,1,1])
B=np.array([2,2,2])
C=np.vstack((A,B))
print(C) # vertical stack

print(A.ndim,C.ndim)
print(A.shape,C.shape)

D=np.hstack((A,B)) # horizontal stack
print(D,'\n',D.ndim,'\n',D.shape)

print(A.T) # doesn't work
