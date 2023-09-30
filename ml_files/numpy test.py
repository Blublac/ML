# Python program using numpy
# for some basic mathematical
# operations

import numpy as np

# creating two arrays of rank 2

x= np.array([[1,2],[3,4]])
y= np.array([[5,6],[7,8]])

#creating two arrays of rank 1 
v= np.array([9,10])
w= np.array([11,12])

#inner products of vectors
print (np.dot(v,w),'\n')

#matrix and vector product
print (np.dot(x,v),'\n')

#matrix and matrix product
print(np.dot(x,y))