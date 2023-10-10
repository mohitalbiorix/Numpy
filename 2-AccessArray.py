# Access Array Elements
import numpy as np;

#1-D array access
arr = np.array([1,2,3,4,5]);
print(arr[2])

#2-D array access
arr = np.array([[1,2,3],[4,5,6]]);
print(arr[0,1])

#3-D array acess
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr[0, 1, 2])

# Negative Indexing
# Use negative indexing to access an array from the end.
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print(arr[1,-1])

