#slicing

""" 
Slicing in python means taking elements from one given index to another given index.
We pass slice instead of index like this: [start:end].
We can also define the step, like this: [start:end:step].
If we don't pass start its considered 0
If we don't pass end its considered length of array in that dimension
If we don't pass step its considered 1 """

import numpy as np

#Slicing 1-D array
arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[1:5]) #[2 3 4 5]
print(arr[4:]) #[5 6 7]
print(arr[:4]) #[1 2 3 4]
print(arr[-3:-1]) #[5 6]


#step
# Use the step value to determine the step of the slicing:
arr = np.array([1, 2, 3, 4, 5, 6, 7,1, 2, 3, 4, 5, 6, 7])

print(arr[1:8:2]) #[2,4,6,1]

#Slicing 2-D array
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[1, 1:4])

# 0:2 means return [0,1] means select both row
#second arguments is an index of element
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[0:2, 2])