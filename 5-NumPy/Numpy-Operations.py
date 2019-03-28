import numpy as np

arr = np.arange(0, 11)
print(arr)


# You can run math operations on arrays, and it will modify the matching indexes.
# So index one will be subtracted from index one, and index two will be subtracted from index two.
print(arr - arr)
print(arr + arr)
print(arr * arr)

# You can also run operations on a single scalar number
print(arr - 10)
print(arr + 10)
print(arr * 10)


# Common array methods
print(np.sqrt(arr))      # Returns the square root of all the values
print(np.exp(arr))       # Returns the exponential of all the values
print(np.max(arr))       # Returns the highest value in the array
print(np.min(arr))       # Returns the lowest value in the array
print(np.sin(arr))       # Returns the sine of the array values
print(np.cos(arr))       # Returns the cosine of the array values.
print(np.log(arr))       # Returns the logarithmic values of the array.


