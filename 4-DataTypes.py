""" NumPy has some extra data types, and refer to data types with one character, like i for integers, u for unsigned integers etc. """
""" 
i - integer
b - boolean
u - unsigned integer
f - float
c - complex float
m - timedelta
M - datetime
O - object
S - string
U - unicode string
V - fixed chunk of memory for other type ( void ) """

import numpy as np

arr = np.array([1, 2, 3, 4])
print(arr.dtype) #int64

arr = np.array(['apple', 'banana', 'cherry'])
print(arr.dtype)

#create array with define data type
arr = np.array([1, 2, 3, 4], dtype='S')

print(arr)
print(arr.dtype)

#Converting Data Type on Existing Arrays
# The astype() function creates a copy of the array, and allows you to specify the data type as a parameter.
arr =  np.array([1.1, 1.2, 1.3]);
newarr = arr.astype('i');
print(newarr) # [1,1,1]
print(newarr.dtype) #int32

newarr = arr.astype(int);
print(newarr) # [1,1,1]
print(newarr.dtype) #int64

arr =  np.array([1,0,3]);
newarr = arr.astype(bool);
print(newarr)
print(newarr.dtype)