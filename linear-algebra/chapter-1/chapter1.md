# Vectors Part 1

- **Dimensionality:**

    The number of elements in the vector.

    Dimensionality is often indicated using \( \mathbb{R}^N \), where \( \mathbb{R} \) indicates real-valued numbers (cf. \( \mathbb{C} \) for complex-valued numbers) and \( N \) indicates the dimensionality. For example, a vector with two elements is said to be a member of \( \mathbb{R}^2 \). That special \( \mathbb{R} \) character is made using LaTeX code, but you can also write \( R^2 \).

- **Orientation:**

    Whether the vector is in column orientation (standing up tall) or row orientation (laying flat and wide).

- **Transpose:**

    Converting a row vector to a column vector and vice versa.

    $$
    m_{i,j} = m_{j,i}
    $$

- **Vector Magnitude:**

    Length or norm of a vector.

    $$
    \| v \| = \sqrt{\sum_{i=1}^{n} v_i^2}
    $$

- **Vector Dot Product:**

    Multiplication of two vectors.

    $$
    \delta = \sum_{i=1}^{n} a_i b_i
    $$

    Example dot product calculation:

    $$
    \begin{align*}
    1 \cdot 5 + 2 \cdot 6 + 3 \cdot 7 + 4 \cdot 8 &= 5 + 12 + 21 + 32 \\
    &= 70
    \end{align*}
    $$

    The dot product is distributive. The distributive property of mathematics is that \(a(b + c) = ab + ac\). Translated into vectors and the vector dot product, it means that:

    $$
    \mathbf{a}^T(\mathbf{b} + \mathbf{c}) = \mathbf{a}^T\mathbf{b} + \mathbf{a}^T\mathbf{c}
    $$

- **Hadamard Multiplication:**
    
    Element-wise multiplication of two vectors.

    
- **Orthogonal Vector Decomposition:**

    Decomposition of a vector into two orthogonal (perpendicular) components.

    Given a vector \( \mathbf{v} \) and a subspace spanned by a vector \( \mathbf{u} \), the orthogonal decomposition of \( \mathbf{v} \) is:

    $$
    \mathbf{v} = \mathbf{v}_{\parallel} + \mathbf{v}_{\perp}
    $$

    where \( \mathbf{v}_{\parallel} \) is the projection of \( \mathbf{v} \) onto \( \mathbf{u} \), and \( \mathbf{v}_{\perp} \) is the component of \( \mathbf{v} \) orthogonal to \( \mathbf{u} \).

    The projection \( \mathbf{v}_{\parallel} \) is given by:

    $$
    \mathbf{v}_{\parallel} = \frac{\mathbf{v} \cdot \mathbf{u}}{\mathbf{u} \cdot \mathbf{u}} \mathbf{u}
    $$

    The orthogonal component \( \mathbf{v}_{\perp} \) is:

    $$
    \mathbf{v}_{\perp} = \mathbf{v} - \mathbf{v}_{\parallel}
    $$

    This decomposition is useful in various applications, such as finding the closest point in a subspace to a given vector.
