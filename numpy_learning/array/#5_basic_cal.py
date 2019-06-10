import numpy as np

a=np.array([10,20,30,40])
b=np.arange(4)
c=a-b
print(a,b,c)
d=b**2 # b^2
print(d)
f=10*np.sin(a)
print(f)

print(b<3) # return a boolean list
print(b==3)

a1=np.array([[11,3],[2,4]])
b1=np.arange(4).reshape((2,2))
print(a1,'\n',b1)
c1=np.dot(a1,b1) # matrices multiplication; innerproduct
c3=a1.dot(b1) # alternative expression
c2=a1*b1 # multiplication one by one
print(c1,'\n',c2)
print(c3)

a2=np.random.random((2,4))
print(a2)
print(np.sum(a2))
print(np.min(a2))
print(np.max(a2))
# axis = 0 -> colunm ; axis = 1 -> row
print("sum of colunm:", np.sum(a2, axis=0))
print("sum of row:", np.sum(a2, axis=1))
print("max of row:", np.max(a2, axis=1))
print("max of colunm:", np.max(a2, axis=0))
