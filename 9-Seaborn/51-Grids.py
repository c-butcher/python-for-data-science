import seaborn as sns
import matplotlib.pyplot as plt

iris = sns.load_dataset('iris')
print(iris.head())

# Pair Plot automatically gives you a grid of multiple plots
# It is basically all scatter plots except the diagonal, which is a bar plot.
sns.pairplot(iris)
plt.show()

# Pair Grid allows you to customise the pair plot grid.
# You can use different plot functions to the upper, lower and diagonal sections.
grid = sns.PairGrid(iris)
grid.map_diag(sns.distplot)    # This will use distributed plots on the diagonal
grid.map_upper(sns.stripplot)  # This will use strip plots above the diagonal line.
grid.map_lower(sns.kdeplot)    # This will use kde plots below the diagonal line.
plt.show()

tips = sns.load_dataset('tips')

# Facet Grid allows you to create multiple graphs based on rows and columns of variables.
# It also allows you to customize the type of plots that you use.
grid = sns.FacetGrid(tips, col='time', row='smoker')
grid.map(sns.distplot, 'total_bill')
plt.show()

# When you create a FacetGrid with a plot that requires multiple columns, such as a scatter
# You just need to pass the second column name, in this case 'tips'.
grid = sns.FacetGrid(tips, col='time', row='smoker')
grid.map(plt.scatter, 'total_bill', 'tip')
plt.show()
