import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')

# This create a linear model plot, which displays a linear fit (estimatation line)
# above the data. You can also use the 'hue' argument to break the data down into categories.
# You can also change the point markers to change the shape of the points.
# Since Seaborn calls matplotlib under the hood, you can also pass in matplotlib arguments, such as scatter_kws.
sns.lmplot(x='total_bill', y='tip', data=tips, hue='sex', markers=['o', 'x'], scatter_kws={'s': 10})
plt.show()


# If you don't want the 'sex' column to be overlapping in a single graph, you can use the 'col' keyword
# and that will create a new graph for each different 'sex'. You can also create new rows of graphs based
# on another categorical value. You can also use the 'hue', which displays to many
sns.lmplot(x='total_bill', y='tip', data=tips, col='sex', row='time', hue='day')
plt.show()


# If the size of the graphs aren't what you need, then you can change the aspect ratio and size.
sns.lmplot(x='total_bill', y='tip', data=tips, col='day', hue='sex', aspect=0.6, size=8)
plt.show()
