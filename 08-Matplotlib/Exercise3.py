import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 100)
y = x * 2
z = x ** 2

# Create the figure
figure = plt.figure()

# Create a new axes (0, 0, 1, 1) didn't work because it hid the x and y numbers.
axes_one = figure.add_axes([0.12, 0.1, 0.8, 0.8])
axes_one.plot(x, z)
axes_one.set_ylabel('Z')
axes_one.set_xlabel('X')
axes_one.set_xlim([0, 100])
axes_one.set_ylim([0, 10000])

axes_two = figure.add_axes([0.25, 0.5, 0.3, 0.3])
axes_two.plot(x, y)
axes_two.set_title('zoom')
axes_two.set_ylabel('Y')
axes_two.set_xlabel('X')
axes_two.set_xlim([20, 22])
axes_two.set_ylim([30, 50])

plt.show()

