import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 100)
y = x * 2
z = x ** 2

# Create the figure
figure = plt.figure()

# Create a new axes (0, 0, 1, 1) didn't work because it hid the x and y numbers.
axes = figure.add_axes([0.1, 0.1, 0.8, 0.8])

# Plot the data points
axes.plot(x, y)

# Set the labels
axes.set_title('title')
axes.set_ylabel('y')
axes.set_xlabel('x')

# Set the limits so the line extends from the very bottom left to the very top right.
axes.set_xlim([0, 100])
axes.set_ylim([0, 200])

plt.show()
