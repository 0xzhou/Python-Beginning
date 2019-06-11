import numpy as np

a=np.arange(2,14).reshape((3,4))
print(a)

a_max=np.argmax(a) # return the index of maximum element
a_min=np.argmin(a) # 返回索引
print(a_max,'\n',a_min)

# mean value


# sum and difference:
print(np.cumsum(a)) # return a list =[Sum1, Sum2, Sum3, Sum4 ...]
print(np.diff(a)) #

print(np.nonzero(a)) # strange function

np.sort(a) # sort in a row; from small to large

print(np.transpose(a))
print(a.T.dot(a)) # a_t * a

print(np.clip(a,5,9)) # set a_i<5 to 5, a_i > 9 to 9

print(np.mean(a,axis=0)) # calculate the average of every column, axis = 1 is for every row
