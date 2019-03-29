import numpy as np
import pandas as pd

# Create a series from two lists
ser = pd.Series([10, 20, 30], ['a', 'b', 'c'])
print(ser)

# Create a Series from an array
ser = pd.Series(np.array([10, 20, 30]))
print(ser)

# Create a Series from a dictionary
ser = pd.Series({'a': 10, 'b': 20, 'c': 30})
print(ser)

# Series can hold strings as their data
ser = pd.Series(['a', 'b', 'c'])
print(ser)

# Series can also hold functions as their data
ser = pd.Series([sum, print, len])
print(ser)

# Create two new series with the data labeled as countries.
ser1 = pd.Series([1, 2, 3, 4], ['USA', 'Germany', 'USSR', 'Japan'])
ser2 = pd.Series([1, 2, 5, 4], ['USA', 'Germany', 'Italy', 'Japan'])
print(ser1)
print(ser2)

# You can lookup series data by the label.
print(ser1['USA'])

# When the data does not have a label, then you can use indexes to grab the data
ser3 = pd.Series(data=['a', 'b', 'c'])
print(ser3[0])

# You can perform operations on series, but when a label exists in one series, but not the other,
# then it will return NaN (non-a-number).
print(ser1 + ser2)
