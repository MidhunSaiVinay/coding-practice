import numpy as np
import matplotlib.pyplot as plt

# Exercise 2-1
# Define vectors
v1 = np.array([2, 1])
v2 = np.array([1, 3])

# Vector sum and difference
v_sum = v1 + v2
v_diff = v1 - v2

# Plot vectors
plt.figure()
plt.quiver(0, 0, v1[0], v1[1], angles='xy', scale_units='xy', scale=1, color='r', label='v1')
plt.quiver(0, 0, v2[0], v2[1], angles='xy', scale_units='xy', scale=1, color='b', label='v2')
plt.quiver(0, 0, v_sum[0], v_sum[1], angles='xy', scale_units='xy', scale=1, color='g', label='v1 + v2')
plt.quiver(0, 0, v_diff[0], v_diff[1], angles='xy', scale_units='xy', scale=1, color='m', label='v1 - v2')

# Plot lines to form triangles
plt.plot([v1[0], v_sum[0]], [v1[1], v_sum[1]], 'g--')
plt.plot([v2[0], v_sum[0]], [v2[1], v_sum[1]], 'g--')
plt.plot([v1[0], v_diff[0]], [v1[1], v_diff[1]], 'm--')
plt.plot([v2[0], v_diff[0]], [v2[1], v_diff[1]], 'm--')

# Set plot limits
plt.xlim(-1, 5)
plt.ylim(-1, 5)

# Add grid, legend, and labels
plt.grid()
plt.legend()
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Vector Sum and Difference')

# Show plot
plt.show()
