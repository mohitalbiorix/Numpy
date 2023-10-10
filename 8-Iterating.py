""" Iterating Arrays

Iterating means going through elements one by one.

As we deal with multi-dimensional arrays in numpy, we can do this using basic for loop of python.

If we iterate on a 1-D array it will go through each element one by one.

 """

import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])

for x in arr:
  for y in x:
    print(y)

# Iterating Arrays Using nditer()
# The function nditer() is a helping function that can be used from very basic to very advanced iterations
arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

for x in np.nditer(arr):
  print(x) # 1,2,3,4,5,6

""" We can use op_dtypes argument and pass it the expected datatype to change the datatype of elements while iterating.

NumPy does not change the data type of the element in-place (where the element is in array) so it needs some other space to perform this action, that extra space is called buffer, and in order to enable it in nditer() we pass flags=['buffered']. """

for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
  print(x)


# Enumerated Iteration Using ndenumerate()

# Enumeration means mentioning sequence number of somethings one by one.

# Sometimes we require corresponding index of the element while iterating, the ndenumerate() method can be used for those usecases.

arr = np.array([[1,2,3,4],[5,6,7,8]]);

for idx, x in np.ndenumerate(arr):
    print(idx,x)