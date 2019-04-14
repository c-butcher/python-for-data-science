import numpy as np
import pandas as pd


from numpy.random import randn
np.random.seed(101)

# Create our data
df = pd.DataFrame(randn(5, 4), ['A', 'B', 'C', 'D', 'E'], ['W', 'X', 'Y', 'Z'])
print(df)

# You can find all of the cells which are greater than zero by doing a comparison on the entire data frame.
booldf = df > 0
print(booldf)

# Then you can get all the values that are above zero, by passing in the comparison booleans.
# When a cell does not meet the condition, then it returns NaN.
print(df[booldf])

# You can also do conditions for a single column.
print(df['W'])
print(df['W'] > 0)

# When you want to filter rows by a column value, you can pass a comparison of that column into the data frame
# This will return only the rows that match the condition
print(df[df['W'] > 0])


# Filtering by column (W) returns a data frame, which you can then retrieve multiple columns (Y, X)
# This looks ugly!
print(df[df['W'] > 0][['Y', 'X']])

# This does the same thing above, but separated into multiple steps. It's a little easier to read,
# but still not very aesthetically pleasing.
boolseries = df['W'] > 0
result = df[boolseries]
print(result[['Y', 'X']])


# When doing multiple conditions for a data frame, you must use the ampersand, rather than the 'and' notation.
# This is because pythons 'and' notation only recognizes boolean values, and the data frame returns another data frame.
# The ampersand most likely executes a magic method on the data frame that has logic for combining conditions.
result = df[(df['W'] > 0) & (df['Y'] > 1)]
print(result)

# You can also use the pipe operator to handle conditional or statements.
result = df[(df['W'] > 0) | (df['Y'] > 1)]
print(result)


# You can reset the index of the data frame so that it uses scalar values, and the older labels will be
# moved to a new column named 'index'.
print(df.reset_index())

# Here we are adding a new column named 'States', which has five values (one per row)
df['States'] = 'CA NY WY OR CO'.split()
print(df)

# Now we can set the indexes to the states column.
df.set_index('States', inplace=True)
print(df)
