# Dynamic Programming

Dynamic Programming (DP) is a method for solving complex problems by breaking them down into simpler subproblems. It is applicable when the subproblems overlap, meaning that the same subproblems are solved multiple times.

## Recursive Algorithm Design Paradigm

1. **Subproblem**: Break the original problem into smaller, manageable subproblems.
2. **Relate**: Find the relationship between the subproblems and the original problem.
3. **Topological Order**: Solve the subproblems in a specific order, ensuring that each subproblem is solved before it is needed.
4. **Base Case**: Identify the simplest subproblems and solve them directly.
5. **Original Problem**: Use the solutions of the subproblems to solve the original problem.
6. **Time Analysis**: Analyze the time complexity to ensure the algorithm is efficient.

Dynamic Programming is particularly useful for optimization problems where you want to find the best solution among many possible solutions.

# Fibonacci Numbers

Given `n`, compute the `n`-th Fibonacci number.

**Recurrence Relation**:
\[ F(n) = F(n-1) + F(n-2) \]
*Explanation*: Each Fibonacci number is the sum of the two preceding numbers in the sequence.

with base cases:
\[ F(1) = F(2) = 1 \]
*Explanation*: The sequence starts with the first two Fibonacci numbers defined as 1.

**Subproblem**: \( F(i) = F_i \) for \( 1 \leq i \leq n \)
*Explanation*: The problem is divided into calculating the Fibonacci number at each position `i` up to `n`.

**Relation**: \( F(i) = F(i-1) + F(i-2) \)
*Explanation*: This relation defines how each Fibonacci number is derived from its two immediate predecessors.

**Topological Order**: Increasing \( i \) for \( i = 1, 2, 3, \ldots \)
*Explanation*: Subproblems are solved in ascending order to ensure that all necessary previous computations are available.

**Original Problem**: \( F(n) \)
*Explanation*: The main objective is to determine the Fibonacci number at the `n`-th position.

**Time Complexity**: \( T(n) = T(n-1) + T(n-2) \)
*Explanation*: The time complexity grows exponentially due to the recursive nature of computing each Fibonacci number.

###Big Idea in dynamic Programming 

Memoization 
Remember and reuse solutions to sub problem

- maintain a dictionary mapping subproblem to their solutions

