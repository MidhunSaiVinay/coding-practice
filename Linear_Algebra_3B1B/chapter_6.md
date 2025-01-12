# The Determinant

The determinant is a scalar value that represents how a linear transformation affects area (in 2D) or volume (in 3D). It measures both the scaling factor and orientation change.

## Key Concepts

1. **Area Scaling**: The determinant tells us how much the area/volume changes after transformation
    - If |det| = 2, area is scaled by factor of 2
    - If |det| = 1/2, area is shrunk by factor of 1/2

2. **Sign Significance**:
    - Positive determinant: Preserves orientation
    - Negative determinant: Reverses orientation

## Calculating Determinants

### 2D Determinant
For a 2×2 matrix A = $\begin{bmatrix} a & b \\ c & d \end{bmatrix}$

det(A) = ad - bc

### 3D Determinant
For a 3×3 matrix A = $\begin{bmatrix} a & b & c \\ d & e & f \\ g & h & i \end{bmatrix}$

det(A) = a(ei-fh) - b(di-fg) + c(dh-eg)

## Properties

1. **Multiplicative Property**: For matrices A and B
    - det(AB) = det(A) × det(B)
    
2. **Inverse Relationship**: 
    - det(A⁻¹) = 1/det(A)

3. **Rotation**: 
    - Pure rotation: |det| = 1
    - In 3D: Right-hand rule determines positive orientation

> Note: A transformation is invertible if and only if its determinant is non-zero.