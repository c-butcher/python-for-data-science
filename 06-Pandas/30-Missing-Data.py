import numpy as np
import pandas as pd

# Create our data frame from a dictionary.
data = {'A': [1, 2, np.nan], 'B': [5, np.nan, np.nan], 'C': [1, 2, 3]}
df = pd.DataFrame(data)
print(df)


# Dropna() will drop all rows that have a NaN value.
print(df.dropna())

# In order to drop the columns, you would change the axis to one.
print(df.dropna(axis=1))

# You can decide how many rows needs to have a NaN, before the row is dropped.
# If the row has two or more NaN's, the row will be dropped.
print(df.dropna(thresh=2))

# You can also fill in the NaN values with a default value.
print(df.fillna(value=False))

# You can also fill in the NaN values for a column with the mean value of that column.
print(df['A'].fillna(value=df['A'].mean()))
