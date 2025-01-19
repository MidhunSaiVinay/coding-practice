#Exercise 2-2
import numpy as np
a= np.array([1, 2, 3])
c=0
for i in a:
    c+=i**2
print(np.sqrt(c))
v_mag = np.linalg.norm(a)
print(v_mag) 