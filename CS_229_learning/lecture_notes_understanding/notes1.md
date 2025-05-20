# CS229 Machine Learning - Course Notes 1

## Introduction to Machine Learning

### Supervised Learning
- Learning from labeled training data
- Two main categories:
    - Regression: Predicting continuous values
    - Classification: Predicting discrete categories

### Linear Regression
- Hypothesis function: h(x) = θ₀ + θ₁x
- Cost function: J(θ) = (1/2m)Σ(h(x) - y)²
- Goal: Minimize cost function using gradient descent

### Gradient Descent
- Algorithm to minimize cost function
- Update rule: θⱼ := θⱼ - α∂/∂θⱼJ(θ)
- Learning rate (α) determines step size

### Normal Equation
- Alternative to gradient descent
- Directly solve for optimal parameters
- θ = (XᵀX)⁻¹Xᵀy

### Key Concepts
- Feature scaling and mean normalization
- Learning rate selection
- Convergence criteria
- Batch vs. stochastic gradient descent

## References
- CS229 Stanford Course Materials
- Machine Learning by Andrew Ng

*Note: These are basic introductory concepts from CS229's first lecture notes.*