""" The Difference Between Copy and View

The main difference between a copy and a view of an array is that the copy is a new array, and the view is just a view of the original array.

The copy owns the data and any changes made to the copy will not affect original array, and any changes made to the original array will not affect the copy.

The view does not own the data and any changes made to the view will affect the original array, and any changes made to the original array will affect the view. 

"""

import numpy as np

#copy : not affect original array
arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
x[0] = 42

print(x)
print(arr)

#view: affect original array
arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
x[0] = 42

print(x)
print(arr)

# Check if Array Owns its Data
# we can check it using base attribute
arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
y = arr.view()
print(x.base); #None
print(y.base); #[1, 2, 3, 4, 5]

#Flattening the arrays
# Flattening array means converting a multidimensional array into a 1D array.

arr = np.array([[1, 2, 3], [4, 5, 6]])

newarr = arr.reshape(-1)

print(newarr)