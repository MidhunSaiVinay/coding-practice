
def squared_norm(vector):
    dot_product = sum([x * x for x in vector])
    return dot_product

# Example usage
vector = [1, 2, 3, 4]
print("Squared Norm:", squared_norm(vector))