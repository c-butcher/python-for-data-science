import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')
flights = sns.load_dataset('flights')

print(tips.head())
print(flights.head())

# Matrix's should be plotted as heat maps
# In order to do that, we need the columns, and rows to have variable indexes.
# The quickest way to do that, is to find the correlation between the data.
tips_corr = tips.corr()

# You can then display the heatmap.
# The annot argument tells whether to display the value in each cell.
sns.heatmap(tips_corr, annot=True)
plt.show()


# Next we want to use pivot table to group numbers by month and year based on the passengers value.
# Pivot table is very useful for organising data.
flight_data = flights.pivot_table(index='month', columns='year', values='passengers')
print(flight_data.head())


# We can customize our heat maps by giving a cmap argument that takes a palette color.
# You can also specify the line color and line width to separate the cells and make
# it easier to see the data.
sns.heatmap(flight_data, cmap='coolwarm', linecolor='white', linewidths=2)
plt.show()

# Cluster maps will move the columns and indexes around so that similar columns and indexes are next to each-other.
# You can also change the standard_scale from 0 (being rows) to 1 (being columns), which will convert each row
# or column to the percentage that it represents.
sns.clustermap(flight_data, cmap='coolwarm', linecolor='white', linewidths=2, standard_scale=1)
plt.show()
