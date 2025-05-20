# inverse matrices column space and null space

## Key Concepts
- Inverse matrix undoes the transformation of original matrix
- Only square matrices can have inverses
- Not all square matrices have inverses (singular/degenerate matrices)

## Conditions for Inverse
- Matrix A is invertible if A⁻¹A = AA⁻¹ = I
- Determinant must not be zero
- Column vectors must be linearly independent

## Column Space
- Set of all possible outputs Ax
- Span of column vectors
- For 2x2 matrix: plane, line, or point

## Null Space
- All vectors x where Ax = 0
- For invertible matrix: only zero vector
- For non-invertible: contains non-zero vectors

## Computation Formulas
For 2x2 matrix:
```
A = [a b]
    [c d]

A⁻¹ = (1/(ad-bc)) * [ d  -b]
                     [-c   a]
```
Where (ad-bc) is determinant

## Rank
- Number of linearly independent rows/columns
- Equals dimension of column space
- After transformation:
    - Rank 2: spans a plane
    - Rank 1: spans a line
    - Rank 0: maps to a point
- Cannot exceed smaller of number of rows or columns
## Full Rank
- Matrix has full rank when rank equals number of rows/columns
- For square matrix: rank equals matrix size
- Full rank matrices are always invertible
- All columns/rows are linearly independent
- Determinant is non-zero
- Column space equals entire target space

