# cross product in light of linear transformation
## Understanding Cross Products Through Linear Transformations

The cross product of two vectors in 3D space can be viewed through the lens of linear transformations, providing a more intuitive understanding.

### Key Concepts

1. The cross product `a × b` results in a vector perpendicular to both input vectors
2. The magnitude equals the area of the parallelogram formed by the vectors
3. Direction follows the right-hand rule

### Linear Transformation Perspective

- Cross product can be expressed as a matrix multiplication:
```
[a × b] = [0   -a₃  a₂ ][b₁]
          [a₃   0  -a₁ ][b₂]
          [-a₂  a₁  0  ][b₃]
```

### Properties

- Anti-commutative: `a × b = -(b × a)`
- Distributive: `a × (b + c) = (a × b) + (a × c)`
- Not associative: `(a × b) × c ≠ a × (b × c)`

### Geometric Interpretation

1. Magnitude: `|a × b| = |a||b|sin(θ)`
2. Direction: Perpendicular to plane containing a and b
3. Orientation: Determined by right-hand rule