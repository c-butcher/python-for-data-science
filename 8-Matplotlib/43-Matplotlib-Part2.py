import matplotlib.pyplot as plt
import numpy as np

# Data for our plots
x_axis = np.linspace(0, 5, 11)
y_axis = x_axis ** 2

# Create the figure and axes.
# We are using tuple unpacking to get the figure and axes in a single call.
# When you have multiple columns or rows, the axes variable will be an array.
figure, axes = plt.subplots(nrows=1, ncols=2)

axes[0].plot(x_axis, y_axis)
axes[0].set_title('First Plot')

axes[1].plot(y_axis, x_axis)
axes[1].set_title('Second Plot')

plt.show()

# You can control the dimensions of the figure by passing in the figsize argument.
figure = plt.figure(figsize=(8, 2))
axes = figure.add_axes([0, 0, 1, 1])
axes.plot(x_axis, y_axis)

plt.show()

# You can also use figsize with the subplots.
figure, axes = plt.subplots(nrows=2, ncols=1, figsize=(8, 2))
axes[0].plot(x_axis, y_axis)
axes[1].plot(y_axis, x_axis)

# The tight_layout() method will make sure the axes don't overlap each-other.
plt.tight_layout()
plt.show()


# You can easily save the figure using the savefig() method.
# The matplotlib library will generate the correct file type based on its extension.
figure.savefig('data/figure2.jpg', dpi=300)
figure.savefig('data/figure1.png', dpi=300)


figure = plt.figure()

# When you create more than one line on an axes, then you might need to create a legend.
# In order to create the legend, each plot must have a label.
ax = figure.add_axes([0, 0, 1, 1])
ax.plot(x_axis, x_axis ** 2, label='Squared')
ax.plot(x_axis, x_axis ** 3, label='Cubed')

# You must call the legend() method to create the legend, and you can specify a location.
# You can use text based locations 'best', 'upper right' and 'lower left', or you can use
# a tuple with a percentage representing the x and y position.
ax.legend(loc=(0.1, 0.1))

plt.show()

