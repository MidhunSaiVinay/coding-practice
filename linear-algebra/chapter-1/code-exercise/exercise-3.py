import math

def calculate_magnitude(vector):
    return math.sqrt(sum([component**2 for component in vector]))

def unit_vector(vector):
    magnitude = calculate_magnitude(vector)
    return [component / magnitude for component in vector]

# Example usage
vector = [0,0]


if calculate_magnitude(vector) == 0:
    print("The zero vector does not have a unit vector.")
else:
    unit_vec = unit_vector(vector)
    print("Unit vector:", unit_vec)