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