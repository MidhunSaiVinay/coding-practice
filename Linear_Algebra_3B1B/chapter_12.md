# Cramer's Rule

Cramer's Rule is a method used to solve systems of linear equations using determinants. While Gaussian elimination is another common approach, each has its advantages in different scenarios.

## Overview
- Used for solving systems of linear equations
- Requires the system's determinant to be non-zero
- Alternative to Gaussian elimination

## Important Notes
- When determinant ≠ 0: Unique solution exists
- When determinant = 0:
    - System may have infinitely many solutions
    - System may have no solutions

## Related Concepts
- Orthonormal matrices
    - A matrix whose columns or rows are orthogonal unit vectors
    - Properties:
        - All vectors are perpendicular to each other
        - All vectors have magnitude of 1

        ## Gaussian Elimination

        Gaussian elimination is a systematic method to solve systems of linear equations by transforming the augmented matrix into row echelon form.

        ### Steps
        1. Write the system as an augmented matrix
        2. Convert to row echelon form:
            - Make leading entries 1
            - Create zeros below each leading 1
        3. Back-substitute to find solutions

        ### Example
        For the system:
        ```
        2x + y = 5
        x - y = 1
        ```

        Augmented matrix:
        ```
        [2  1 | 5]
        [1 -1 | 1]
        ```

        Row operations:
        ```
        R1 - 2R2 → R1:
        [0  3 | 3]
        [1 -1 | 1]
        ```

        Solution:
        - y = 1
        - x = 2