import pandas as pd

df1 = pd.DataFrame({
    'A': ['A0', 'A1', 'A2', 'A3'],
    'B': ['B0', 'B1', 'B2', 'B3'],
    'C': ['C0', 'C1', 'C2', 'C3'],
    'D': ['D0', 'D1', 'D2', 'D3']
}, index=[0, 1, 2, 3])

df2 = pd.DataFrame({
    'A': ['A4', 'A5', 'A6', 'A7'],
    'B': ['B4', 'B5', 'B6', 'B7'],
    'C': ['C4', 'C5', 'C6', 'C7'],
    'D': ['D4', 'D5', 'D6', 'D7']
}, index=[4, 5, 6, 7])

df3 = pd.DataFrame({
    'A': ['A8', 'A9', 'A10', 'A11'],
    'B': ['B8', 'B9', 'B10', 'B11'],
    'C': ['C8', 'C9', 'C10', 'C11'],
    'D': ['D8', 'D9', 'D10', 'D11']
}, index=[8, 9, 10, 11])

# First we are going to show the original data
print(df1)
print(df2)
print(df3)

# Then we are going to concatenate them together. This will append the data from data frames 2 and 3, into the first
# data frame. Adding all data as a new row.
concatted = pd.concat([df1, df2, df3])
print(concatted)


# You can also concatenate the data so it is added as a new column.
# This will create empty values if the data frame doesn't have matching indexes.
concatted = pd.concat([df1, df2, df3], axis=1)
print(concatted)


# We are now creating new data from our merging examples
left = pd.DataFrame({
    'key': ['K0', 'K1', 'K2', 'K3'],
    'key2': ['K1', 'K2', 'K3', 'K4'],
    'A': ['A0', 'A1', 'A2', 'A3'],
    'B': ['B0', 'B1', 'B2', 'B3']
})

right = pd.DataFrame({
    'key': ['K0', 'K1', 'K2', 'K3'],
    'key2': ['K2', 'K3', 'K4', 'K1'],
    'C': ['C0', 'C1', 'C2', 'C3'],
    'D': ['D0', 'D1', 'D2', 'D3']
})

print(left)
print(right)

# You can merge two data frames together using the merge() method. This uses SQL style keywords to describe how and
# on what column the data should be merged. Very useful for combining columns!
merged = pd.merge(left, right, how='inner', on='key')
print(merged)

# Merging on the right with two keys
merged = pd.merge(left, right, how='right', on=['key', 'key2'])
print(merged)


# Our data for the Joining examples.
left = pd.DataFrame({
    'A': ['A0', 'A1', 'A2'],
    'B': ['B0', 'B1', 'B2']
}, index=['K0', 'K1', 'K2'])

right = pd.DataFrame({
    'C': ['C0', 'C2', 'C3'],
    'D': ['D0', 'D2', 'D3']
}, index=['K0', 'K2', 'K3'])


# The data_frame.join() method joins columns based on the rows indexes.
print(left.join(right))
print(left.join(right, how='outer'))
