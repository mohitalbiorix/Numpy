""" NumPy is a Python library.

NumPy is used for working with arrays.

NumPy is short for "Numerical Python". """


import numpy as np;

# numpy array
# NumPy is used to work with arrays. The array object in NumPy is called ndarray.
arr = np.array([1,2,3,4,5]);
print(arr);

# array using list
arr = np.array([1,2,3,4,5]);
print(arr);

# array using tuple
arr = np.array((1,2,3,4,5));
print(arr);

#Dimensions in Arrays

# 0-D Arrays
arr = np.array(42);
print(arr)

# 1-D array
# An array that has 0-D arrays as its elements is called uni-dimensional or 1-D array.
arr = np.array([1,2,3,4,5]);
print(arr)

# 2-D array
# An array that has 1-D arrays as its elements is called a 2-D array.
arr = np.array([[1,2,3],[4,5,6]]);
print(arr)

# 3-D array
# An array that has 2-D arrays (matrices) as its elements is called 3-D array.
arr = np.array([[[1,2,3],[4,5,6]] , [[1,2,3],[4,5,6]]]);
print(arr)


#ndim arrtibute
# returns an integer that tells us how many dimensions the array have.
a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim);
print(b.ndim);
print(c.ndim);
print(d.ndim);


#ndmin
# we can create any number of dimensions 
arr = np.array([1,2,3,4,5], ndmin=5);
print(arr);
