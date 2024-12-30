import numpy as np
# creating a vector
asList  = [1,2,3]
asArray = np.array([1,2,3]) # 1D array
rowVec  = np.array([ [1,2,3] ]) # row
colVec  = np.array([ [1],[2],[3] ]) # column

print(f'asList:  {np.shape(asList)}')
print(f'asArray: {asArray.shape}')
print(f'rowVec:  {rowVec.shape}')
print(f'colVec:  {colVec.shape}')

# row column vector addition
v = np.array([[4,5,6]]) # row vector
w = np.array([[10,20,30]]).T # column vector
v+w
print(f'v+w: {v+w}')

# Vector scalar multiplication
s = 2
a = [3,4,5] # as list
b = np.array(a) # as np array
print(a*s)
print(b*s)

#vector scalar addition
s = 2
v = np.array([3,6])
print(s+v)

#vector length
v = np.array([1,2,3,7,8,9])
v_dim = len(v)  # math dimensionality
v_mag = np.linalg.norm(v) # math magnitude, length, or norm

print(f'v_dim: {v_dim}')

