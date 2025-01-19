# Nonsquare matrices as transformations between dimensions

In this chapter, we explore how matrices can transform vectors between spaces of different dimensions.

## Key Concepts

1. Non-square matrices represent transformations between spaces of different dimensions
    - An m × n matrix transforms vectors from n-dimensional space to m-dimensional space
    - The columns represent the landing spots of basis vectors

2. Example: 2×3 Matrix
    - Maps vectors from 3D to 2D space
    - Each column represents where unit vectors (î, ĵ, k̂) land in 2D
    - Can be visualized as a "flattening" of 3D space onto a plane

3. Example: 3×2 Matrix
    - Maps vectors from 2D to 3D space
    - Represents embedding a 2D plane into 3D space
    - Output restricted to a 2D plane within 3D space

## Applications

- Computer Graphics: Projecting 3D scenes onto 2D screens
- Data Science: Dimensionality reduction
- Machine Learning: Feature extraction and compression

## Linear Dependencies

- Columns being linearly dependent means the output space is "squished" to a lower dimension
- Full rank means the transformation uses the full dimensionality of the output space