#roots of quadrartic equation only real roots in int

import math
a=int(input())
b=int(input())
c=int(input())
def quadraticRoots(a, b, c):
    # Calculate the discriminant
    discriminant = b**2 - 4*a*c
        
        # Calculate roots based on the discriminant
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
            
            # Return the floor values in decreasing order
        return [math.floor(max(root1, root2)), math.floor(min(root1, root2))]
    elif discriminant == 0:
        root = -b / (2*a)
            
            # Return the floor value
        return [math.floor(root),math.floor(root)]
    else:
        
        return print("Imaginary")
print(quadraticRoots(a, b, c))