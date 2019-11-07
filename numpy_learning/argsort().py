'''
numpy.argsort(a, axis=-1, kind=None, order=None):
a--array-like

output--array of indices the sorted elment

'''
import numpy as np
x=np.array([3,1,2])
xs=x.argsort()
print(xs)
