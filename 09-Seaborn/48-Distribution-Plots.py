import seaborn as sns
import matplotlib.pyplot as plt

# Seaborn has built in data-sets, this one has to do with restaurant tips.
tips = sns.load_dataset('tips')

# Just wanted to start by calculating the percentage of the tip compared to the total bill.
tips['tip_percent'] = round((tips['tip'] / tips['total_bill']) * 100, 2)
print(tips.head())

# Creates a distribution graph that shows the number of each total_bills
# Bins will break the data down to 30 separate bars.
sns.distplot(tips['total_bill'], kde=False, bins=30)
plt.show()

# Joint Plots allow you to view the distribution of two data points, such as total bill vs tips.
# You can also change the kind of graph that is displayed.
# kind='reg' is a linear regression graph that displays a regression line.
# kind='hex' breaks the graph into hexagons, and
# kind='kde' displays a distributed heat map.
sns.jointplot(tips['total_bill'], tips['tip'], kind='kde')
plt.show()

# Pair Plot shows distributed graphs for all numerical fields (total_bill, tip, size)
# The hue is used to categorize the data by a specific field, giving a different color to each value.
# For instance, using hue='sex', will make all the Male's one color and the Female's another color.
# The palette option allows you to use color themes to display the data.
sns.pairplot(tips, hue='sex', palette='deep')
plt.show()


# KDE stands for Kernel Density Estimation
# Apparently it's the sum of all the Normal Distributions of each point.

# Rug Plot draws small dashes where each point is on the graph.
sns.rugplot(tips['total_bill'])
plt.show()
