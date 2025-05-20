# Perceptron and Generalized linear model
## The Perceptron Learning Algorithm

The perceptron algorithm is a historical machine learning model that attempts to force binary (0 or 1) outputs, unlike logistic regression which produces probabilities.

### Key Components:
- Uses a threshold function g(z):
    - g(z) = 1 if z ≥ 0
    - g(z) = 0 if z < 0
- Hypothesis function: hθ(x) = g(θᵀx)
- Update rule: θⱼ := θⱼ + α(y⁽ⁱ⁾ - hθ(x⁽ⁱ⁾))x⁽ⁱ⁾ⱼ

### Historical Context
- Developed in 1960s
- Intended to model individual neuron behavior
- Serves as a foundational model for learning theory

### Limitations
- Lacks meaningful probabilistic interpretations
- Cannot be derived through maximum likelihood estimation
- Fundamentally different from logistic regression and linear regression
# Generalised linear model
## exponential Family
 exponential family s pdf probability distribution function can be written as 
             p(y; η) = b(y)exp(ηTT(y) − a(η))

η- is natural parameter
y- data because we use exponential family to model output of our data
T(y)-sufficient stastic
b(y)- base measure
a(η) - log partition
in exponential family the equation should integrate to 1

