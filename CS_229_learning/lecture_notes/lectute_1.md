# Linear Regression

## Definition
Linear regression is a fundamental statistical model that predicts a continuous target variable by finding the best-fitting linear relationship between input features and outputs. It assumes a linear relationship between variables and minimizes the sum of squared differences between predicted and actual values.

## Key Components
- Dependent variable (y)
- Independent variables (x)
- Coefficients (weights)
- Error term (residuals)

## Process of Supervised Learning Algorithm
1. Start with a training set
2. Feed data into supervised learning algorithm
3. Generate a hypothesis function
4. Use hypothesis to predict output values for new inputs

> Note: The hypothesis function maps any input to a predicted output value based on patterns learned during training.

## Hypothesis Function
In linear regression, the hypothesis function h(x) is represented as:

h(x) = θ₀ + θ₁x₁ + θ₂x₂ + ... + θₙxₙ

Where:
- θᵢ are the model parameters (weights)
- xᵢ are the input features
- θ₀ is the bias term (intercept)

This can also be written in matrix form:

h(x) = ∑(θᵢxᵢ) = θᵀx

Where:
- x = [1, x₁, x₂, ..., xₙ]ᵀ (with x₀ = 1)
- θ = [θ₀, θ₁, θ₂, ..., θₙ]ᵀ

## Key Notations
- θ (theta): Model parameters/weights that need to be learned
- m: Number of training examples (rows) in the dataset
- x: Input features/variables in the model
- y: Output or target variable
- (x,y): A training example pair where x is the input and y is the output
- (x⁽ⁱ⁾,y⁽ⁱ⁾): The i-th example in the training set
- n: Number of features (input variables) in the model
## Parameter Selection
The goal in linear regression is to choose parameters θ that make h(x) approximate y as closely as possible.

### Cost Function
In linear regression, we minimize the squared differences between predictions and actual values. This is known as the Ordinary Least Squares (OLS) method.

The cost function J(θ) is defined as:

J(θ) = (1/2) ∑ᵢ₌₁ᵐ (hθ(x⁽ⁱ⁾) - y⁽ⁱ⁾)²

Where:
- hθ(x) is the hypothesis function with parameters θ
- x⁽ⁱ⁾ is the i-th input feature vector
- y⁽ⁱ⁾ is the i-th target value
- m is the number of training examples
- The factor 1/2 is included to simplify the derivative calculations

The objective is to find values of θ that minimize J(θ).


## To find the value of θ that minimizes cost function J(θ), we are going to use gradient descent.

## Gradient Descent
The gradient descent algorithm iteratively updates θ to minimize J(θ):

1. Initialize θ to zeros
2. Repeat until convergence:
    - θⱼ := θⱼ - α(∂/∂θⱼ)J(θ) for j = 0,...,n
    - Update all θⱼ simultaneously
    ### Convergence
    Convergence occurs when subsequent iterations of gradient descent produce minimal changes in parameter values (θ), indicating that the algorithm has found a local minimum of the cost function. This typically happens when:

    - The magnitude of parameter updates becomes very small
    - The cost function J(θ) stabilizes and shows negligible improvement
    - The gradient (∂/∂θⱼ)J(θ) approaches zero

Where:
- α is the learning rate
- ∂/∂θⱼ denotes partial derivative
- := represents parameter update

The update rule for each iteration:
θⱼ := θⱼ - α∑ᵢ₌₁ᵐ(hθ(x⁽ⁱ⁾) - y⁽ⁱ⁾)x⁽ⁱ⁾ⱼ


### Gradient Descent Visualization

```
Cost J(θ)
    ↑
    |     *
    |   *   *
    | *       * 
    |*           *
    |              *
    |                 *
    |                    *
    |                      *___
    |                         *____
    +--------------------------------→ θ
    
    * = Path taken by gradient descent
```

A step-by-step process:

1. Initialize θ parameters
    - Start with random or zero values
    
2. Calculate Cost J(θ)
    - Measure current prediction errors
    
3. Compute Gradient ∇J(θ)
    - Determine direction of steepest descent
    
4. Update Parameters θ
    - Take a step in the negative gradient direction
    
5. Check Convergence
    - If not converged, return to step 2
    - If converged, use final parameters

### Learning Rate Effects
- Too Small α: Very slow convergence
- Too Large α: May overshoot and diverge
- Optimal α: Efficient convergence to minimum

## Batch Gradient Descent
Batch gradient descent uses the entire training dataset to compute the gradient for each parameter update.

### Definition
- Updates parameters using all m training examples in each iteration
- Computes the average gradient across entire dataset
- More stable but computationally expensive for large datasets

### Usage
- Small to medium-sized datasets
- When computational resources aren't constrained
- When solution stability is prioritized over speed
- Problems requiring high precision in parameter estimation

## Stochastic Gradient Descent

### Definition
Stochastic gradient descent (SGD) updates parameters using a single training example per iteration:
- Randomly selects one training example
- Updates parameters based on gradient from that example
- Faster but less stable than batch gradient descent
- More likely to escape local minima due to noise in updates

### Usage
- Large datasets where batch gradient descent is computationally expensive
- Online learning scenarios where data arrives sequentially
- Problems where approximate solutions are acceptable
- Cases where escaping local minima is beneficial
- Real-time or streaming applications
