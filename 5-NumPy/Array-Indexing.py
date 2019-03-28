import numpy as np

# Get an array with the range of 0 - 10
arr = np.arange(0, 11)
print(arr)
print(arr[8])          # Retrieves index 8
print(arr[1:5])        # Retrieves indexes 1 - 5
print(arr[:5])         # Retrieves everything before index 5.
print(arr[5:])         # Retrieves everything after index 5.


# Change indexes 0-5 to have the value 100
arr[0:5] = 100
print(arr)


# Create an array with 0-10, then slice it so we only get the first 5 indexes.
# Change the sliced array so all values are set to 99.
# Notice how the original array was changed. This is because slicing the array makes a pointer.
arr = np.arange(0, 11)
sliced_arr = arr[0:5]
sliced_arr[:] = 99
print(sliced_arr)
print(arr)


# Create a new array with values from 0-10. We then make a copy of that array, so we can change
# the copy, without actually changing the original.
arr = np.arange(0, 11)
arr_copy = arr.copy()
arr_copy[:] = 100
print(arr)
print(arr_copy)


# Create a 2-dimensional array
arr_2d = np.array([[5, 10, 15], [20, 25, 30], [35, 40, 45]])
print(arr_2d)
print(arr_2d[0][0])      # Grab the five value from the first array
print(arr_2d[2][1])      # Grab the forty value from the last array.
print(arr_2d[1, 2])      # Grab the thirty value from from the middle array.

# Returns a sub-section of the array. Everything before the last row, and after the first column.
print(arr_2d[:2, 1:])
print(arr_2d[1:, :2])    # Grab everything after the first row, and before the last column.
print(arr_2d[:, 1:2])    # Grab the middle column (10, 25, 40)


# Create an array, and then compare all values in the array.
# This returns an array of booleans, telling whether each value is greater than 5, or not.
arr = np.arange(1, 11)
comparison = arr > 5
print(comparison)
print(arr[comparison])  # Returns only the values that are greater than five.
print(arr[arr > 5])     # Another, easier way to get the values that are greater than five.
print(arr[arr < 3])     # Returns all the values that are less than three.


# Create a 2-dimensional array with five rows and ten columns
arr_2d = np.arange(50).reshape(5, 10)
print(arr_2d)

# Grab a small section of that array
chunk = arr_2d[1:4, 2:8]
print(chunk)
print(chunk[chunk >= 25])    # Grab only the values that are greater than or equal to 25.


