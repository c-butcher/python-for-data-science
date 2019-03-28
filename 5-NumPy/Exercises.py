# Import numpy
import numpy as np

print()
print('Create an array of ten zeros')
zeros = np.zeros(10)
print(zeros)


print()
print('Create an array of ten ones')
ones = np.ones(10)
print(ones)


print()
print('Create an array of 10 fives')
fives = np.ones(10) * 5
print(fives)


print()
print('Create an array of all the even integer from 10 to 50')
ints = np.arange(10, 51, 2)
print(ints)


print()
print('Create a 3x3 matrix with values ranging from 0 to 8')
matrix = np.arange(0, 9).reshape(3, 3)
print(matrix)


print()
print('Create a 3x3 identity matrix')
identity = np.eye(3)
print(identity)


print()
print('Use NumPy to generate an array of 25 random numbers sampled from a standard normal distribution.')
normalized = np.random.randn(25)
print(normalized)


print()
print('Create the following matrix.')
matrix = np.arange(0, 1.01, 0.01)
print(matrix)


print()
print('Create an array of 20 linearly spaced points between 0 and 1.')
arr = np.linspace(0, 1, 20)
print(arr)


print()
print('Pull out a subsection of the matrix...')
mat = np.arange(1, 26).reshape(5, 5)
print(mat[2:, 1:])


print()
print('Now pull out the number twenty...')
print(mat[3, 4])


print()
print('Now pull out the first three results of the second column...')
print(mat[0:3, 1:2])


print()
print('Now pull out the last row...')
print(mat[4])


print()
print('Now pull out the last two rows...')
print(mat[3:5])


print()
print('Get the sum of all the values in mat')
print(mat.sum())


print()
print('Get the standard deviation of the values in mat')
print(mat.std())


print()
print('Get the sum of all the columns in the mat')
print(mat.sum(axis=0))
