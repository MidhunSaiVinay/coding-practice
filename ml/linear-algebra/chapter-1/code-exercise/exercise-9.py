import numpy as np
import matplotlib.pyplot as plt

# Generate random vectors t and r
t = np.random.rand(2)
r = np.random.rand(2)

# Orthogonal decomposition
t_parallel_r = np.dot(t, r) / np.dot(r, r) * r
t_perpendicular_r = t - t_parallel_r 

# Plotting
plt.quiver(0, 0, t[0], t[1], angles='xy', scale_units='xy', scale=1, color='r', label='t')
plt.quiver(0, 0, r[0], r[1], angles='xy', scale_units='xy', scale=1, color='b', label='r')
plt.quiver(0, 0, t_parallel_r[0], t_parallel_r[1], angles='xy', scale_units='xy', scale=1, color='g', label='t_parallel_r')
plt.quiver(0, 0, t_perpendicular_r[0], t_perpendicular_r[1], angles='xy', scale_units='xy', scale=1, color='y', label='t_perpendicular_r')

plt.xlim(-1, 2)
plt.ylim(-1, 2)
plt.axhline(0, color='grey', lw=0.5)
plt.axvline(0, color='grey', lw=0.5)
plt.grid(True)
plt.legend()
plt.show()

# Confirm orthogonality
print("t:", t)
print("r:", r)
print("t_parallel_r:", t_parallel_r)
print("t_perpendicular_r:", t_perpendicular_r)
print("Sum of components:", np.allclose(t, t_parallel_r + t_perpendicular_r))
print("Orthogonality:", np.isclose(np.dot(t_perpendicular_r, r), 0))
# Show orthogonal vector decomposition
fig, ax = plt.subplots()
ax.quiver(0, 0, t[0], t[1], angles='xy', scale_units='xy', scale=1, color='r', label='t')
ax.quiver(0, 0, r[0], r[1], angles='xy', scale_units='xy', scale=1, color='b', label='r')
ax.quiver(0, 0, t_parallel_r[0], t_parallel_r[1], angles='xy', scale_units='xy', scale=1, color='g', label='t_parallel_r')
ax.quiver(t_parallel_r[0], t_parallel_r[1], t_perpendicular_r[0], t_perpendicular_r[1], angles='xy', scale_units='xy', scale=1, color='y', label='t_perpendicular_r')

ax.set_xlim(-1, 2)
ax.set_ylim(-1, 2)
ax.axhline(0, color='grey', lw=0.5)
ax.axvline(0, color='grey', lw=0.5)
ax.grid(True)
ax.legend()
plt.show()