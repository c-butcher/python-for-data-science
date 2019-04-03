import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')

# You can change the grid style by calling sns.set_style().
# Either pass in a string (darkgrid, whitegrid, dark, white, ticks)
# or you can pass in a dictionary with style values.
# https://seaborn.pydata.org/generated/seaborn.set_style.html?highlight=set_style#seaborn.set_style
sns.set_style('whitegrid')
sns.countplot('sex', data=tips)
plt.show()

# Using the despine method allows you to remove the borders around the plot.
# By default it will remove the top and right sides, but you can also specify the left and bottom.
sns.set_style(None)
sns.countplot('sex', data=tips)
sns.despine(left=True, bottom=True)
plt.show()

# Since seaborn is built on top of matplot lib, you can change the figsize using matplot lib,
# and it will also change the figsize of the seaborn plots. This most likely works with a lot
# of the matplot lib configurations.
plt.figure(figsize=(12, 3))
sns.countplot('sex', data=tips)
plt.show()


# You can define the context of why you're creating the graph. For instance, you might be printing it to
# a 'poster', or using it for a 'talk'. By default the context is for 'notebook'.
sns.set_context('poster', font_scale=1.5)
sns.countplot('sex', data=tips)
plt.show()


# You can change the palette using the matplotlib color maps.
# https://matplotlib.org/gallery/color/colormap_reference.html
sns.set_context('notebook', font_scale=1)
sns.lmplot(x='total_bill', y='tip', data=tips, hue='sex', palette='ocean')
plt.show()
