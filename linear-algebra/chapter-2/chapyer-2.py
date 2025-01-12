#Linear weighted combination of vectors
import numpy as np
l1 = 1
l2 = 2
l3 = -3
v1 = np.array([4,5,1])
v2 = np.array([-4,0,-4])
v3 = np.array([1,3,2])
print(l1*v1 + l2*v2 + l3*v3)

#code Exercises

#Exercise 3-1

scalars = [1, 2, -3]
vectors = [np.array([4, 5, 1]), np.array([-4, 0, -4]), np.array([1, 3, 2])]

result = np.zeros(3)
for scalar, vector in zip(scalars, vectors):
    result += scalar * vector

print(result)

#Exercise 3-2
scalars = [1, 2, -3, 4]
vectors = [np.array([4, 5, 1]), np.array([-4, 0, -4]), np.array([1, 3, 2]), np.array([2, 2, 2, 2])]

result = np.zeros(4)
for scalar, vector in zip(scalars, vectors):
    if len(vector) != len(result):
        print(f"Vector {vector} has a different dimension than the result vector.")
        continue
    result += scalar * vector

print(result)

#Exercise 3-3

import plotly.graph_objects as go

# Define the vector set containing one vector [1, 3]
basis_vector_2d = np.array([1, 3])

# Create 100 random scalars from a uniform distribution between -4 and +4
random_scalars_2d = np.random.uniform(-4, 4, 100)

# Multiply the random scalars by the basis vector to create 100 random points in the subspace
random_points_2d = np.array([scalar * basis_vector_2d for scalar in random_scalars_2d])

# Plot the points
fig_2d = go.Figure(data=[go.Scatter(x=random_points_2d[:, 0], y=random_points_2d[:, 1], mode='markers')])
fig_2d.show()

# Define the vector set containing two vectors in R^3
basis_vectors_3d = [np.array([3, 5, 1]), np.array([0, 2, 2])]

# Create 100 x 2 random scalars from a uniform distribution between -4 and +4
random_scalars_3d = np.random.uniform(-4, 4, (100, 2))

# Multiply the random scalars by the basis vectors to create 100 random points in the subspace
random_points_3d = np.array([scalars[0] * basis_vectors_3d[0] + scalars[1] * basis_vectors_3d[1] for scalars in random_scalars_3d])

# Plot the points
fig_3d = go.Figure(data=[go.Scatter3d(x=random_points_3d[:, 0], y=random_points_3d[:, 1], z=random_points_3d[:, 2], mode='markers')])
fig_3d.show()

# Repeat the R^3 case but setting the second vector to be 1/2 times the first
basis_vectors_3d_half = [np.array([3, 5, 1]), 0.5 * np.array([3, 5, 1])]

# Multiply the random scalars by the basis vectors to create 100 random points in the subspace
random_points_3d_half = np.array([scalars[0] * basis_vectors_3d_half[0] + scalars[1] * basis_vectors_3d_half[1] for scalars in random_scalars_3d])

# Plot the points
fig_3d_half = go.Figure(data=[go.Scatter3d(x=random_points_3d_half[:, 0], y=random_points_3d_half[:, 1], z=random_points_3d_half[:, 2], mode='markers')])
fig_3d_half.show()