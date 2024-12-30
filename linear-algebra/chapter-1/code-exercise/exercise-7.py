def dot_product(a, b):
    return sum(x * y for x, y in zip(a, b))

# Example usage
a = [1, 2, 3]
b = [4, 5, 6]

dot_ab = dot_product(a, b)
dot_ba = dot_product(b, a)

print("a . b:", dot_ab)
print("b . a:", dot_ba)
print("Dot product is commutative:", dot_ab == dot_ba)
