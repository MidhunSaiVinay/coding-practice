# Vectors Part 2

- **Vector Sets:**

    A vector set is a set of vectors.

- **Linear Weighted Combination:**

    Linear weighted combination is a combination of scalar vector multiplication and addition.

    $$\[ w = \lambda_1 v_1 + \lambda_2 v_2 + \ldots + \lambda_n v_n \]$$

- **Linear weighted combination applications:**
    - **Applications in Statistical Models:**
        The predicted data from a statistical model are created by taking the linear weighted combination of regressors (predictor variables) and coefficients (scalars) computed via the least squares algorithm.

    - **Dimension-Reduction Procedures:**
        In procedures such as principal components analysis, each component is derived as a linear weighted combination of the data channels, with weights selected to maximize the variance of the component.

    - **Artificial Neural Networks:**
        Neural networks involve a linear weighted combination of input data followed by a nonlinear transformation. The weights are learned by minimizing a cost function, typically the difference between the model prediction and the real-world target variable.

- **Linear Independence:**
    A set of vectors is **linearly dependent** if at least one vector in the set can be expressed as a linear weighted combination of other vectors in that set. Conversely, a set of vectors is **linearly independent** if no vector can be expressed as a linear weighted combination of other vectors in the set.

    - **Subspace and Span:**

        When introducing linear weighted combinations, specific numerical values for the weights were used (e.g., λ1=1, λ3=−3). A subspace is the same idea but using the infinity of possible ways to linearly combine the vectors in the set. For some (finite) set of vectors, the infinite number of ways to linearly combine them—using the same vectors but different numerical values for the weights—creates a vector subspace. The mechanism of combining all possible linear weighted combinations is called the span of the vector set.

        - **Example 1:**
            A vector set containing one vector:
            $$ V = \begin{bmatrix} 1 \\ 3 \end{bmatrix} $$
            The span of this vector set is the infinity of vectors that can be created as linear combinations of the vectors in the set. For a set with one vector, that simply means all possible scaled versions of that vector.

        - **Example 2:**
            A set of two vectors in ℝ3:
            $$ V = \left\{ \begin{bmatrix} 1 \\ 0 \\ 2 \end{bmatrix}, \begin{bmatrix} -1 \\ 1 \\ 2 \end{bmatrix} \right\} $$
            The vectors are in ℝ3, so they are graphically represented in a 3D axis. But the subspace that they span is a 2D plane in that 3D space. That plane passes through the origin, because scaling both vectors by zero gives the zero vector.

        - **Example 3:**
            Two vectors in ℝ3:
            $$ V = \left\{ \begin{bmatrix} 1 \\ 1 \\ 1 \end{bmatrix}, \begin{bmatrix} 2 \\ 2 \\ 2 \end{bmatrix} \right\} $$
            The subspace that they span is still only a 1D subspace—a line. This is because one vector in the set is already in the span of the other vector, making one of the two vectors redundant in terms of span.

        The dimensionality of the subspace spanned by a set of vectors is the smallest number of vectors that forms a linearly independent set. If a vector set is linearly independent, then the dimensionality of the subspace spanned by the vectors in that set equals the number of vectors in that set. If the set is dependent, then the dimensionality of the subspace spanned by those vectors is necessarily less than the number of vectors in that set.

        The formal definition of a vector subspace is a subset that is closed under addition and scalar multiplication, and includes the origin of the space. This means that any linear weighted combination of vectors in the subspace must also be in the same subspace, including setting all weights to zero to produce the zero vector at the origin of the space.

        - **Difference Between Subspace and Span:**
            Span is the mechanism of creating a subspace. A set of vectors spans, and the result of their spanning is a subspace. Span and subspace often refer to identical mathematical objects, and using the terms interchangeably is usually correct.

- **Basis:**
    A basis is a set of vectors that can be used to describe a space. It acts like a ruler for measuring the space.

    - **Example:**
        The most common basis set is the Cartesian axis: the familiar XY plane. The basis sets for 2D and 3D Cartesian graphs are:
        $$ S_2 = \left\{ \begin{bmatrix} 1 \\ 0 \end{bmatrix}, \begin{bmatrix} 0 \\ 1 \end{bmatrix} \right\} $$
        $$ S_3 = \left\{ \begin{bmatrix} 1 \\ 0 \\ 0 \end{bmatrix}, \begin{bmatrix} 0 \\ 1 \\ 0 \end{bmatrix}, \begin{bmatrix} 0 \\ 0 \\ 1 \end{bmatrix} \right\} $$

    - **Alternative Basis Set:**
        Another basis set for ℝ2:
        $$ T = \left\{ \begin{bmatrix} 3 \\ 1 \end{bmatrix}, \begin{bmatrix} -3 \\ 1 \end{bmatrix} \right\} $$
        Both S2 and T span the same subspace (all of ℝ2), but T can provide a more compact and orthogonal description for certain data points.

    - **Importance in Data Science:**
        Bases are crucial in data science and machine learning. Many problems can be conceptualized as finding the best set of basis vectors to describe some subspace. Techniques like dimension reduction, feature extraction, principal components analysis, and others are essentially ways of identifying optimal basis vectors for a specific problem.

    - **Definition of Basis:**
        A set of vectors can be a basis for some subspace if it (1) spans that subspace and (2) is an independent set of vectors. A basis needs to span the space it is used for and must be linearly independent to ensure unique coordinates for any vector in the subspace.