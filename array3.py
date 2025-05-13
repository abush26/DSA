import numpy as np
a = np.array([ [1,2] ,
      [3,4],
      [5,6]])
print(a)
# Finding Dimension/rank of array
print(a.ndim)
print(a.dtype)
# Flatten function
b = a.flatten()
print(b)
# Reshape Function
c = a.reshape(2,3)
print(c)
# concatenate Function
x = np.array([1,2,3])
y = np.array([4,5,6])
z = x + y
print(z)