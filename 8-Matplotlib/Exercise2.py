import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 100)
y = x * 2
z = x ** 2

# Create the figure
figure = plt.figure()

# Create a new axes (0, 0, 1, 1) didn't work because it hid the x and y numbers.
axes_one = figure.add_axes([0.1, 0.1, 0.8, 0.8])
axes_one.plot(x, y, color='red')
axes_one.set_xlim([0, 100])
axes_one.set_ylim([0, 200])
axes_one.set_ylabel('y')
axes_one.set_xlabel('x')

axes_two = figure.add_axes([0.2, 0.5, 0.2, 0.2])
axes_two.plot(x, y, color='red')
axes_two.set_xlim([0, 100])
axes_two.set_ylim([0, 200])
axes_two.set_ylabel('y')
axes_two.set_xlabel('x')
axes_two.set_yticks(np.linspace(0, 200, 5))
axes_two.set_xticks(np.linspace(0, 100, 6))

plt.show()

