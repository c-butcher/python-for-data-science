import numpy as np
import pandas as pd

data = {
    'Company': ['GOOG', 'GOOG', 'MSFT', 'MSFT', 'FB', 'FB'],
    'Person': ['Sam', 'Charlie', 'Amy', 'Vanessa', 'Carl', 'Sarah'],
    'Sales': [200, 120, 340, 124, 243, 350]
}

df = pd.DataFrame(data)
print(df)

# When you use df.groupby(), it returns a DataFrameGroupBy object
byCompany = df.groupby('Company')
print(byCompany)


# When you call the groupby.mean() method, it returns a new data frame, which contains all the columns
# that are numbers and discards all others.
means = byCompany.mean()
sums = byCompany.sum()
stds = byCompany.std()
print(means)
print(sums)
print(stds)

# The max() and min() methods will order all columns, including strings, and return the last result.
maxs = byCompany.max()
mins = byCompany.min()
print(maxs)
print(mins)


# You can also get the indexes value, just like any other data frame.
print(maxs.loc['GOOG'])
print(mins.loc['FB'])


# The teacher suggests to put it all the code on a single line.
# Personally, it depends on whether it looks good in the code and is readable.
print(df.groupby('Company').sum().loc['FB'])


# This is awesome, the describe method calculates the count, mean, std, min, 25%, 50%, 75% and max.
# You can even transpose it, which turns the columns into rows, and the rows into columns.
print(df.groupby('Company').describe())
print(df.groupby('Company').describe().transpose())
