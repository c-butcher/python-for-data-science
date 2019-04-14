import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 100)
y = x * 2
z = x ** 2

# Create two graphs next to each other.
figure, axes = plt.subplots(nrows=1, ncols=2)
axes[0].plot(x, y, color='blue', linewidth=2, linestyle='--')
axes[0].set_xlim([0, 100])
axes[0].set_ylim([0, 200])

axes[1].plot(x, z, color='red', linewidth=2)
axes[1].set_xlim([0, 100])
axes[1].set_ylim([0, 10000])

plt.tight_layout()
plt.show()


# Create the same graphs, but this time changing the figure size to (8 ,2)
figure, axes = plt.subplots(nrows=1, ncols=2, figsize=(8, 2))
axes[0].plot(x, y, color='blue', linewidth=2)
axes[0].set_xlim([0, 100])
axes[0].set_ylim([0, 200])

axes[1].plot(x, z, color='red', linewidth=2, linestyle='--')
axes[1].set_xlim([0, 100])
axes[1].set_ylim([0, 10000])

plt.tight_layout()
plt.show()