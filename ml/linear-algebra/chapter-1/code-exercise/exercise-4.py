import numpy as np

def scale_vector_to_magnitude(vector, desired_magnitude):
    # Calculate the current magnitude of the vector
    current_magnitude = np.linalg.norm(vector)
    
    # Calculate the scaling factor
    scaling_factor = desired_magnitude / current_magnitude
    
    # Scale the vector
    scaled_vector = vector * scaling_factor
    
    return scaled_vector

# Example usage:
vector = np.array([1, 2, 3])
desired_magnitude = 5
scaled_vector = scale_vector_to_magnitude(vector, desired_magnitude)
print(scaled_vector)