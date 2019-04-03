import seaborn as sns
import matplotlib.pyplot as plt

titanic = sns.load_dataset('titanic')
print(titanic.head())

sns.set_style('whitegrid')

sns.jointplot(x='fare', y='age', data=titanic)
plt.show()


sns.distplot(titanic['fare'], kde=False, bins=30, color='red')
plt.show()


sns.boxplot(x='class', y='age', data=titanic)
plt.show()


sns.swarmplot(x='class', y='age', data=titanic)
plt.show()


sns.countplot(x='sex', data=titanic)
plt.show()


titanic_corr = titanic.corr()
plt.title('titanic.corr()')
sns.heatmap(titanic_corr, cmap='coolwarm')
plt.show()


grid = sns.FacetGrid(data=titanic, col='sex')
grid.map(sns.distplot, 'age', kde=False, bins=10)
plt.show()
