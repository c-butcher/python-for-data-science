import numpy as np
import pandas as pd
from numpy.random import randn

# Makes sure random generated numbers will always be the same.
np.random.seed(101)

# Data frames are matrix's of data with labels for both the rows and columns.
df = pd.DataFrame(randn(5, 4), ['A', 'B', 'C', 'D', 'E'], ['W', 'X', 'Y', 'Z'])
print(df)

# Retrieves an entire column of information
# Each column in the DataFrame is nothing more than a Series.
print(df['W'])
print(type(df['W']))

# You can also retrieve two columns at a time by passing a list.
print(df[['W', 'Z']])


# You can create new columns by simply adding a new index to the data frame.
df['TOTAL'] = df['W'] + df['X'] + df['Y'] + df['Z']
print(df)

# You can also remove the column by using the drop() method.
# When the axis is set to zero, it removes rows, but when set to 1, then it removes columns
# You'll also need to assign the inplace argument to true, in order to mutate the current DF.
# Without the inplace=True, then will won't mutate the original data frame, and instead return a new one.
df.drop('TOTAL', axis=1, inplace=True)
print(df)

# You can also drop a row
print(df.drop('E'))

# You can get the shape of the data frame as a tuple.
print(df.shape)

# You can get a row of data using the DataFrame.loc[] list/array using a single label, or list of labels.
print(df.loc['A'])
print(df.loc[['A', 'B']])

# You can also lookup a row by index using the DataFrame.iloc[] list/array.
print(df.iloc[0])

# You can retrieve a single piece of datum by supplying the row and column to the DataFrame.loc[] list/array.
print(df.loc['B', 'Y'])

# Or you can retrieve multiple rows and columns by supply a list of rows and list of columns.
print(df.loc[['A', 'B'], ['W', 'Y']])

