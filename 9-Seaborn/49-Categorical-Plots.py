import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')
print(tips.head())


# Bar plots compare two different columns, and can group by numerical or string value.
# The estimator normally uses the mean value (average) to compare, but you can change
# the estimator function to use other calculations, such as standard deviations.
sns.barplot('sex', 'total_bill', data=tips, estimator=np.std)
plt.show()


# Count plots will show you the total number of values for a single column.
# This will show a bar graph with how many Male and Female rows of data there are.
sns.countplot(x='sex', data=tips)
plt.show()


# Box plot categorizes/groups by the x-axis, and then shows the distribution of the y-axis.
# In this graph, we will see the total_bill range for each day.
# The box itself contains the core distribution (most populated area)
# The whiskers show the rest of the distribution
# The points outside the whiskers are outliers.
# When you add the hue, it will break each category into sub-categories based on smoker vs non-smoker.
sns.boxplot(x='day', y='total_bill', data=tips, hue='smoker')
plt.show()


# Violin Plots show much more information.
sns.violinplot(x='day', y='total_bill', data=tips, hue='sex', dodge=True)
plt.show()


# Strip Plots display all the points, but sometimes they overlap. You can turn on
# the jitter option to add some noise to their horizontal position, but it won't necessarily
# stop them from overlapping.
sns.stripplot(x='day', y='total_bill', data=tips, hue='sex', dodge=True, jitter=True)
plt.show()


# Swarm plots will make sure that points do not overlap each-other, and instead place them next to each-other.
# Unfortunately they don't scale very well to a large data-set.
sns.swarmplot(x='day', y='total_bill', data=tips, hue='sex', dodge=True)
plt.show()

# You can also combine two plots so they are overlaid on top of each-other.
sns.violinplot(x='day', y='total_bill', data=tips, hue='sex', dodge=True)
sns.swarmplot(x='day', y='total_bill', data=tips, hue='sex', dodge=True, color='black')
plt.show()


# Factor plot is a generic way of calling categorical plots.
# You can change the type of graph that is displayed by changing the
# kind argument to 'bar', 'violin', 'swarm', etc.
sns.factorplot(x='day', y='total_bill', data=tips, kind='violin')
plt.show()


# NOTE: Factor Plot has been deprecated will be removed soon.
# Instead you should use catplot()
sns.catplot(x='day', y='total_bill', data=tips, kind='swarm')
plt.show()
