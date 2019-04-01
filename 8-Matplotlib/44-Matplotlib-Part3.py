import matplotlib.pyplot as plt
import numpy as np

# Data for our plots
x_axis = np.linspace(0, 5, 11)
y_axis = x_axis ** 2


# Create our figure and our axes.
# You can specify the color as an argument in the plot() method, using either color string, or rgb hex values.
figure, axes = plt.subplots()
axes.plot(x_axis, y_axis, color='#00AA88')
axes.plot(x_axis, x_axis ** 2.5, linewidth=2)     # Change the line width
axes.plot(x_axis, x_axis ** 3, alpha=0.5)         # Change the transparency of the line
axes.plot(x_axis, x_axis ** 3.5, linestyle='--')  # Change the line style using (-- or -. or : or 'steps')

# Markers can also be placed on plot points, and stylized.
axes.plot(
    x_axis,
    y_axis * 10,
    color='purple',
    marker='o',
    markersize=5,
    markerfacecolor='yellow',
    markeredgewidth=1,
    markeredgecolor='purple'
)

# You can set limits for the x and y axes.
# Just pass in a list with the lower bound, and upper bound.
axes.set_xlim([0, 5])
axes.set_ylim([0, 250])

plt.show()

