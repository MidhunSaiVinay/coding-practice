# Locally Weighted & Logistic Regression

## Locally Weighted Regression

There are two types of ML algorithms:

1. **Parametric Algorithms**
    - Fit fixed set of parameters to data
    - Example: Linear regression

2. **Non-parametric Algorithms**
    - Example: Locally weighted regression
    - Amount of data/parameters grows linearly with size of data

In locally weighted regression, we focus on the local area around our prediction point. Points closer to our prediction point have more weight.

We fit θ to minimize the modified cost function:

```
J(θ) = Σ(i=1 to m) w(i) * (y(i) - θᵀx(i))²
```

where weight function:
```
w(i) = exp(-(x(i)-x)²/(2τ²))
```

Properties:
- If ||x(i)-x|| is small, then w(i) ≈ 1
- If ||x(i)-x|| is large, then w(i) ≈ 0

The bandwidth parameter τ controls:
- How many examples influence the prediction
- Trade-off between overfitting and underfitting

## Probabilistic Interpretation of Linear Regression

Why least squares?

When using linear regression with least-squares cost function, we make these assumptions:

1. Target variables and inputs are related by:
    ```
    y(i) = θᵀx(i) + ε(i)
    ```
    where ε(i) represents error terms

2. Error terms ε(i) are:
    - IID (independently and identically distributed)
    - Follow Gaussian distribution N(0,σ²)
    - Have mean zero and variance σ²

Under these assumptions:
- P(y(i)|x(i);θ) ~ N(θᵀx(i),σ²)
- Maximum likelihood estimation leads to:
  ```
  J(θ) = (1/2)Σ(y(i) - θᵀx(i))²
  ```

Note: Final θ is independent of σ²

## Logistic Regression

Linear regression is unsuitable for classification. Instead, we use logistic regression where:

```
h(x) = g(θᵀx) = 1/(1 + e^(-z))
```
where g(z) is the sigmoid/logistic function

Probability equations:
```
P(y=1|x;θ) = hθ(x)
P(y=0|x;θ) = 1 - hθ(x)
```

For y ∈ {0,1}:
```
P(y|x;θ) = (hθ(x))^y * (1-hθ(x))^(1-y)
```

Likelihood function:
```
L(θ) = Π(i=1 to m) P(y(i)|x(i);θ)
      = Π(i=1 to m) (hθ(x(i)))^y(i) * (1-hθ(x(i)))^(1-y(i))
```

We maximize log-likelihood using batch gradient ascent. The function has only one global maximum.

## Newton's Method

Newton's method provides faster convergence than gradient descent:
- Quadratic convergence rate
- Uses function's second derivative
- Each iteration finds where tangent line intersects x-axis
- Repeat until convergence
