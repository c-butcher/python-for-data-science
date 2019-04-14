import numpy as np
import pandas as pd
from numpy.random import randn

# We are creating a multi-indexed data frame.
# First we have our labels for the outside
outside = ['G1', 'G1', 'G1', 'G2', 'G2', 'G2']

# Then we have our labels for the inside. Each number matches up to the label above.
inside = [1, 2, 3, 1, 2, 3]

# We then combine the outside and inside indexes, and create tuples from them.
hier_index = list(zip(outside, inside))
hier_index = pd.MultiIndex.from_tuples(hier_index)
print(hier_index)

# Then we can use that information as our row labels.
df = pd.DataFrame(randn(6, 2), hier_index, ['A', 'B'])
print(df)

# We can then get a subset of the data
print(df.loc['G1'])

# Or we can get a row from that subset
print(df.loc['G1'].loc[1])

# Or we can get a single cell
print(df.loc['G2'].loc[1]['B'])


# You can also name the index columns by changing the index names.
df.index.names = ['Groups', 'Num']
print(df)

# One more time, we are getting a single cells value.
cell = df.loc['G2'].loc[2]['B']
print(cell)

# You can also use the cross-section (xs) command, in order to get the outer subset.
print(df.xs('G1'))

# Or you can use the cross-section command to get the inner subset by telling it what 'level' to look at.
print(df.xs(1, level='Num'))

