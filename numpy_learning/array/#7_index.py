import numpy as np

a=np.arange(3,15)
print(a)
print(a[3]) # like array

b=a.reshape(3,4)
print(b[2]) # return the third row
print(b[2,0]) # return the first element of the third row; [row = n+1,column= m+1]
print(b[2][0])
print(b[1,:]) # ':' represents the all elements
print(b[1,1:3])

# loop:
for row in b: # default output is by row
    print(row)

for row in b.T: # tricky, to output the by column
    print(row)

# every element
c = b.flatten() # transform to 1 dimension
for item in c: # return every element
    print(item)

