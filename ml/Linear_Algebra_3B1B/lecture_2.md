# Linear Combinations, Span, and Basis Vectors

## Unit Vectors
- $\hat{i}$ is the unit vector along the x-axis, represented as $\begin{pmatrix} 1 \\ 0 \end{pmatrix}$
- $\hat{j}$ is the unit vector along the y-axis, represented as $\begin{pmatrix} 0 \\ 1 \end{pmatrix}$

## Linear Combinations
Any vector in 2D space can be written as a linear combination of $\hat{i}$ and $\hat{j}$:
$\vec{v} = a\hat{i} + b\hat{j}$ where $a$ and $b$ are scalars

### Properties of Linear Combinations:
1. When scaling one vector while keeping the other fixed: 
    - Results in a straight line
2. When scaling both vectors:
    - Can reach any point in the plane (if vectors aren't parallel or zero)

## Span
- The span is the set of all possible linear combinations of given vectors
- For 2D vectors $\vec{v_1}$ and $\vec{v_2}$:
  ```math
  Span(\vec{v_1}, \vec{v_2}) = \{a\vec{v_1} + b\vec{v_2} | a,b \in \mathbb{R}\}
  ```

## Vector Representation
- Vectors can be visualized as arrows from origin to a point
- In 2D: $\vec{v} = \begin{pmatrix} x \\ y \end{pmatrix}$
- In 3D: $\vec{v} = \begin{pmatrix} x \\ y \\ z \end{pmatrix}$

## Linear Dependence and Independence
- Vectors are linearly dependent if one can be expressed as a linear combination of others
- Vectors are linearly independent if no vector can be expressed as a linear combination of others

![Linear Combinations in 2D](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Linear_combination.svg/400px-Linear_combination.svg.png)

