# Eigen vector and eigen value
## Introduction
- Eigenvectors are special vectors that, when transformed, only get stretched or squished (scaled)
- The scaling factor is called the eigenvalue

## Key Concepts
1. For a linear transformation T and vector v:
    - If T(v) = λv (where λ is a scalar)
    - Then v is an eigenvector and λ is its eigenvalue

## Computing Eigenvalues and Eigenvectors
1. For a matrix A:
    - Set up equation: (A - λI)v = 0
    - Find det(A - λI) = 0
    - Solve for λ (eigenvalues)
    - For each λ, solve (A - λI)v = 0 to find v (eigenvectors)

## Example
For matrix A = [[2, 1],
                     [1, 2]]
1. Find det(A - λI) = 0
    - det([[2-λ, 1],
             [1, 2-λ]]) = 0
    - (2-λ)(2-λ) - 1 = 0
    - λ² - 4λ + 3 = 0
    - λ = 3 or λ = 1

2. Find eigenvectors:
    - For λ = 3: solve (A - 3I)v = 0
    - For λ = 1: solve (A - I)v = 0

## Applications
- Principal Component Analysis
- Diagonalization
- Stability Analysis
