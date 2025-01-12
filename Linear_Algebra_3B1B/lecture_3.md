# Linear Transformations and Matrices

## Linear Transformation
A transformation is a function that maps vectors from input space to output space. For a transformation to be considered linear, it must satisfy two key properties:

1. **Linearity**: All lines remain lines (no curves)
2. **Origin Preservation**: Origin stays fixed at (0,0)

These properties ensure grid lines remain parallel and evenly spaced.

## Understanding with Basis Vectors
Let's examine basis vectors:
* î = [1, -2]
* ĵ = [3, 0]
* Vector v = -1î + 2ĵ

**Matrix Notation**:
```python
v = -1[1, -2] + 2[3, 0]
```

### Transformation Process
To determine a vector's position after transformation:
1. Locate transformed positions of î and ĵ
2. Apply linear combination: v_transformed = -1(transformed_î) + 2(transformed_ĵ)

This can be expressed through matrix multiplication:
```python
[a b][x] = [ax + by]
[c d][y]   [cx + dy]
```

## Shear Transformation
A shear transformation maintains certain properties:
* Keeps î vector fixed
* Shifts ĵ to new position
* Creates parallelogram distortion

**Example Shear Matrix**:
```python
[1 1]
[0 1]
```

