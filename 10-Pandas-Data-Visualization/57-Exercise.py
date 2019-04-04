import pandas as pd
import matplotlib.pyplot as plt

df3 = pd.read_csv('data/df3')
print(df3.info())
print(df3.head())

# Create a scatter plot of 'b' vs 'a'.
df3.plot.scatter(x='a', y='b', color='red', figsize=(8, 2))
plt.show()

# Create a histogram from column 'a'.
df3['a'].plot.hist()
plt.show()

# Redoing the last plot using a different style and more bins
plt.style.use('ggplot')
df3['a'].plot.hist(bins=25)
plt.show()

# Create a boxplot comparing the a and b columns.
df3[['a', 'b']].plot.box()
plt.show()

# Create a kde plot of the 'd' column.
df3['d'].plot.kde(color='red', lw=5, linestyle='--')
plt.show()

# Create an area plot of all the columns for just the rows up to 30. (hint: use .ix).
df3.iloc[:30].plot.area()
plt.legend(loc='center right', bbox_to_anchor=(1.15, 0.5))
plt.show()
