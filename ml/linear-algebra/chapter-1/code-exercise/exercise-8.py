import numpy as np

import matplotlib.pyplot as plt


# Projection of b onto a

a = np.array([324, 23])
b = np.array([657, 564])

beta = np.dot(b, a) / np.dot(a, a)
projection = beta * a

# Plotting the vectors
plt.quiver(0, 0, a[0], a[1], angles='xy', scale_units='xy', scale=1, color='r', label='a')
plt.quiver(0, 0, b[0], b[1], angles='xy', scale_units='xy', scale=1, color='b', label='b')
plt.quiver(0, 0, projection[0], projection[1], angles='xy', scale_units='xy', scale=1, color='g', label='Projection of b onto a')

plt.legend()
plt.grid(True)
plt.show()