
import numpy as np

a = np.array([2,23,4],dtype=np.int64) # int32, float32, float64 etc.
print(a,a.ndim)
print(a.dtype)

b=np.array([[1,2,3],
           [44,8,9]]) # default type is int32
print(b,b.dtype)

# define 0-matrice: the default data type here is float64
c=np.zeros((3,4))
print(c,c.dtype)
d=np.ones((2,4))
print(d,d.dtype)
e=np.empty((3,4))
print(e,e.dtype)

f=np.arange(10,20,2) # (start, end, step)
print(f,f.dtype)
g=np.arange(12).reshape((3,4))
print(g,g.dtype)
h=np.linspace(1,10,20) # (start, end, total number of element)
print(h,h.dtype)
