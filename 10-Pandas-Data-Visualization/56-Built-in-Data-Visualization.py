import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# You can apply the index_col argument to sort and label the indexes.
df1 = pd.read_csv('data/df1', index_col=0)
print(df1.head())

# I'm honestly not sure what's happening when you don't supply the index column.
# It looks like the dates are being converted to index values.
df2 = pd.read_csv('data/df2')
print(df2.head())

# Pandas allows for histograms, but you need to call the matplotlib hist() function on the data set.
df1['A'].hist(bins=10)
plt.show()

# You can also use the dataset's plot object to call a specific plot type.
df1['A'].plot.hist()
plt.show()

# You can create an area plot
df2.plot.area(alpha=0.4)
plt.show()

# A bar plot
df2.plot.bar(stacked=True)
plt.show()

# Plot a line
df1.plot.line(y='B', figsize=(8, 2), lw=0.5)
plt.show()

# Scatter plot, the 'c' argument maps a data point so it controls the color of the point.
# You can also use the 's' argument to map a data point so it control the size of the point.
df1.plot.scatter(x='A', y='B', c='C', s=df1['D'] * 10, cmap='coolwarm')
plt.show()

# Box plot
df1.plot.box()
plt.show()

# Creating some random data for our next plot
df = pd.DataFrame(np.random.randn(100, 2), columns=['a', 'b'])
print(df.head())

# Hexagon plot
df.plot.hexbin(x='a', y='b', gridsize=25, cmap='coolwarm')
plt.show()

# Kernel Density plot
df['a'].plot.kde()
plt.show()

# Another way to do the Kernel Density plot
df['b'].plot.density()
plt.show()

