import numpy as np

# Create a list
my_list = [1, 2, 3]
print(my_list)


# Transform the list to an array
arr = np.array(my_list)
print(arr)


# Create a multi-dimensional list and convert it to an array
mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
arr = np.array(mat)
print(arr)


# Create an array from a range, skipping by two
arr = np.arange(0, 11, 2)
print(arr)


# Create an array with all zeros
arr = np.zeros(10)
print(arr)


# Create a multi-dimensional array of 5 rows and 5 columns
arr = np.zeros((5, 5))
print(arr)


# Create an array of ones
arr = np.ones(4)
print(arr)


# Create a multi-dimensional array of ones
arr = np.ones((2, 3))
print(arr)


# Create an array that contains 100 numbers, evenly distributed from zero to five.
arr = np.linspace(0, 5, 100)
print(arr)


# Create a multi-dimensional array with ones going diagonal and zeros everywhere else
arr = np.eye(10)
print(arr)


# Create five random numbers
arr = np.random.rand(5)
print(arr)


# Create a multi-dimensional array using random numbers with 2 rows and 3 columns.
arr = np.random.rand(2, 3)
print(arr)


# Create a multi-dimensional array with normalized numbers using 2 rows and 2 columns.
arr = np.random.randn(2, 2)
print(arr)


# Create a multi-dimensional integer array with random numbers between 1 and 99, using 2 rows and 3 columns.
arr = np.random.randint(1, 100, (2, 3))
print(arr)


# Create an array going from 1-25, and then reshape the array to have 5 rows and 5 columns
# When you reshape, you have to use no more, or no less than the number of indexes
arr = np.arange(1, 26)
arr = arr.reshape(5, 5)
print(arr)
print(arr.shape)


# Create an integer array and then select the minimum and maximum values.
random_arr = np.random.randint(0, 50, 10)
print(random_arr.max())
print(random_arr.min())
print(random_arr[random_arr.argmax()])
print(random_arr[random_arr.argmin()])


# Returns the data type of the array
print(arr.dtype)
print(random_arr.dtype)


# Import a single function from a library
from numpy.random import randint
print(randint(2, 5))
