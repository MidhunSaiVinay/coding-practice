# Cross Product

The cross product of two vectors results in a new vector that is perpendicular to both input vectors. Its magnitude equals the area of the parallelogram formed by the two vectors.

## 2D Cross Product
- For vectors `v` and `w` in 2D space
- Area = determinant of matrix formed by vectors `v` and `w`
- Direction follows right-hand rule

## 3D Cross Product
For vectors `v = (v₁, v₂, v₃)` and `w = (w₁, w₂, w₃)`:

```
v × w = | i  j  k  |
    | v₁ v₂ v₃ |
    | w₁ w₂ w₃ |
```

The result is:
- i(v₂w₃ - v₃w₂)
- j(v₃w₁ - v₁w₃)
- k(v₁w₂ - v₂w₁)

Properties:
- Anticommutative: v × w = -(w × v)
- Magnitude: |v × w| = |v||w|sin(θ)
- Direction: Perpendicular to both v and w
