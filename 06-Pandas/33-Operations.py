import numpy as np
import pandas as pd

df = pd.DataFrame({
    'col1': [1, 2, 3, 4],
    'col2': [444, 555, 666, 444],
    'col3': ['abc', 'def', 'ghi', 'xyz']
})

print(df.head())

# Get the unique values for the column
uniques = df['col2'].unique()
print(uniques)

# You can also get the number of unique values by using either of these methods...
length = len(df['col2'].unique())
print(length)

length = df['col2'].nunique()
print(length)

# You can get the number of times a value appears in the column.
counts = df['col2'].value_counts()
print(counts)

# We are re-iterating conditional selections with a data frame.
greaterThanTwo = df[(df['col1'] > 2) & (df['col2'] == 444)]
print(greaterThanTwo)


# We can apply a function to an entire column by using the data_frame.apply(func_name) method.
def times2(x):
    return x * 2


print(df['col1'].apply(times2))  # Multiples column one by two
print(df['col3'].apply(len))  # Counts the number of characters in the strings of column three.
print(df['col2'].apply(lambda x: x * 2))  # Also works with inline lambda functions

# Re-iterating how to drop a column
print(df.drop('col1', axis=1))

# This will permanently delete the column (inplace)
del df['col1']

# Returns a list of column names
print(df.columns)

# Returns the start, and stop of the index numbers for the columns
print(df.index)

# You can sort the values by column or columns.
print(df.sort_values('col2'))
print(df.sort_values(['col3', 'col2']))

# This method runs a conditional on all columns to check to see if they are null.
# It returns a boolean data frame that tells whether a specific spot is null.
print(df.isnull())


# Our data for the pivot table example.
data = {
    'A': ['foo', 'foo', 'foo', 'bar', 'bar', 'bar'],
    'B': ['one', 'one', 'two', 'two', 'one', 'one'],
    'C': ['x', 'y', 'x', 'y', 'x', 'y'],
    'D': [1, 3, 2, 5, 4, 1]
}

df = pd.DataFrame(data)
print(df)

# Pivot tables allows you to easily create a multi-indexed data frame
pivoted = df.pivot_table(values='D', index=['A', 'B'], columns='C')
pivoted.fillna(0, inplace=True)
print(pivoted)
