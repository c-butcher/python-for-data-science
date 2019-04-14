import matplotlib.pyplot as plt
import numpy as np

# Create our data-points for the x-axis and y-axis.
x_axis = np.linspace(0, 5, 11)
y_axis = x_axis ** 2

# -----------------------
# Functional Oriented Method
# -----------------------

# Give our graph some labels
plt.xlabel('Time (minutes)')
plt.ylabel('Distance (miles)')
plt.title('Time over Distance')

# Add the data to the graph, and show it.
plt.plot(x_axis, y_axis)
plt.show()

# Now we're creating two graphs, subplot-1 and subplot-2
# We are passing in the number of row, number of columns, and the graph we're currently working on.
plt.subplot(1, 2, 1)
plt.plot(x_axis, y_axis, 'r')

# Now we're switching over to our second graph, were we invert the x and y axis, before showing both graphs.
plt.subplot(1, 2, 2)
plt.plot(y_axis, x_axis, 'b')
plt.show()


# -----------------------
# Object Oriented Method
# -----------------------

# A figure is open-space where you can add axes (x/y graphs)
fig = plt.figure()

# You can create the axes by supply the [left, bottom, width, height] where each value is represented as a percentage
# between 0 - 1. So if you set the left to 0.1, that means it is 10% from the left side,
axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])

# We then add our data to the plot points.
axes.plot(x_axis, y_axis)

# And set our labels for the axes.
axes.set_ylabel('Time (milliseconds)')
axes.set_xlabel('Page Loads')
axes.set_title('Page Load Per Second')

plt.show()

# We are now creating two axes on the same figure.
fig = plt.figure()

# Create our first axes (graph)
axes1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
axes1.plot(x_axis, y_axis)
axes1.set_title('Large Plot')

# Create our second axes, which sits on top of the first one and is smaller.
axes2 = fig.add_axes([0.2, 0.5, 0.4, 0.3])
axes2.plot(y_axis, x_axis)
axes2.set_title('Small Plot')

plt.show()
