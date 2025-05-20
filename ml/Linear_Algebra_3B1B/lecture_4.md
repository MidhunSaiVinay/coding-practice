# Matrix Multiplication as Composition 🔄

When we apply two transformations, for example, a rotation followed by a shear, the resulting transformation is a composition of these operations. This powerful concept allows us to combine multiple transformations into a single matrix.

## Understanding Composition 🎯
The new matrix representing this composition transformation captures the final positions of the î and ĵ basis vectors after both transformations are applied, eliminating the need for separate transformation matrices.

## Key Properties 📝
1. **Composition**: Product of transformations
2. **Directionality**: Matrix multiplication flows left to right
3. **Non-commutative**: $M_1M_2 \neq M_2M_1$
4. **Associative**: $(M_1M_2)M_3 = M_1(M_2M_3)$

### Example: Rotation & Shear 🔄↔️
For a rotation matrix $R$ and shear matrix $S$, the composition is expressed as:

$$\text{Final Transform} = S \times R$$

Where:
- $R$ = Rotation matrix
- $S$ = Shear matrix
- $\times$ denotes matrix multiplication

> **Important**: The order of multiplication matters! $SR \neq RS$ in general for matrix transformations.