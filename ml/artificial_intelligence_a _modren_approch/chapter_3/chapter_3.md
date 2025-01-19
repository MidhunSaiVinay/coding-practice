# Solving problems by searching

there are two types of searches informed and un informed

## problem solving agents
for our agent to solve any problem in un known evnoirment agent needs to have a 
- goal formulation the agent adopts a goal and organises behaviour by limiting objectives hence the actions to be considered

- problem formulation the agent devises a description of the states and actions necessary to reach a goal

- search before taking any action the agent simulates each scenario of reaching goal and such sequence is called solution 

- execution now agent can execute the actions shown in solution

write about open and closed loop systems 

### search problem and solution
a search problem can be defined as 
problem
 a set of possible states that enviorment can be state space

 initial state that the agent starts in

 a set or one of goal state 

 actions avilabe to agents

 Atransition model, which describes what each action does. RESULT(s,a) returns the Transition model
 state that results from doing action a in state s

 cost function  cost of each action

 ### formulationg problems

Abstraction is the process of removing unnecessary details from a representation to focus on essential elements. Key aspects include:

- **Level of Detail**: A good problem formulation maintains the right balance of detail
    - Too detailed: "move foot forward 1cm"
    - Too abstract: "travel across country"
    - Optimal: "drive from city A to city B"

- **Valid Abstraction**: An abstraction is valid when:
    - Any abstract solution can be converted to a detailed solution
    - Each abstract action corresponds to executable detailed actions
    - Abstract states map to sets of detailed world states

- **Useful Abstraction**: Characteristics include:
    - Actions are easier to execute than the original problem
    - Essential details are preserved
    - Unnecessary complexities are removed

Proper abstraction prevents agents from being overwhelmed by real-world complexity while maintaining problem solvability.

## Example Problems
 there are two kinds of problems standardised and real world problem


### Standardized Problems

#### Grid World Problems
Grid worlds are 2D rectangular arrays where:
- Agents move between cells (horizontally/vertically, sometimes diagonally)
- Cells may contain objects or obstacles
- Common variants include:
    - Vacuum world: Agent cleans dirty cells
    - Sokoban: Agent pushes boxes to storage locations
    - Sliding puzzles: Tiles slide in a grid with one blank space

#### 8-Puzzle
A classic sliding tile puzzle where:
- 3x3 grid with 8 numbered tiles and one blank
- Goal is to arrange tiles in specific order
- Actions move blank space Up/Down/Left/Right
- Each move costs 1
- Solution exists for half of all possible states

#### Knuth's Problem
An infinite state space problem where:
- Start with number 4
- Apply sqrt, floor, or factorial operations
- Goal is to reach any positive integer
- Shows how simple rules can create complex spaces

### Real world problems
#### Route Finding
- Used in various applications from driving directions to military planning
- Main challenges include traffic delays and road closures
- Complex variants exist for video streaming and airline routing

#### Airline Travel Planning
- States include location, time, and fare history
- Actions involve flight selections considering connections
- Costs factor in money, time, comfort, and rewards
- Must handle contingency planning for delays

#### Touring Problems
- Traveling Salesperson Problem (TSP) optimizes visiting multiple locations
- Applications include:
    - School bus routing
    - Circuit board drilling
    - Shop floor management

#### VLSI Layout
- Positions circuit components to optimize:
    - Area usage
    - Circuit delays
    - Manufacturing yield
- Divided into cell layout and channel routing

#### Robot Navigation
- Generalizes route-finding to continuous spaces
- Challenges include:
    - Multi-dimensional movement
    - Sensor errors
    - Partial observability

#### Assembly Sequencing
- Used in manufacturing since 1970s
- Orders assembly steps for complex objects
- Applications include:
    - Electric motor assembly
    - Protein design
    - Industrial automation

## Search Algorithams

search algoritham takes search problem as input and reti=urns a solution or indication of failure

we need to make a search tree graph so as to over state space graph and each node in search trree corrsponds to a state in the space and the edges in search tree corrspond to actions

### Best-First Search Algorithm

- Algorithm chooses nodes with minimum value of evaluation function f(n)
- Steps:
    1. Select minimum f(n) node from frontier
    2. Check if it's goal state
    3. If not, expand to generate children
    4. Add new children to frontier if not reached before
    5. Re-add if new path cost is lower

### Search Data Structures

#### Node Components
- `STATE`: Current state
- `PARENT`: Node that generated this node
- `ACTION`: Action taken to reach this node
- `PATH-COST`: Total cost from initial state (g(node))

#### Queue Types
- Priority Queue: Pops minimum cost node
- FIFO Queue: First-in-first-out
- LIFO Queue (Stack): Last-in-first-out

### Handling Redundant Paths

Three approaches:
1. Remember all reached states (preferred)
2. Ignore repeats for certain problems
3. Check only for cycles

### Performance Metrics

Four key measures:
1. Completeness: Guaranteed to find solution if exists
2. Cost optimality: Finds lowest cost solution
3. Time complexity: Processing time or states examined
4. Space complexity: Memory requirements

For infinite spaces, systematic search is required for completeness.
### Uninformed Search Strategies

Uninformed search algorithms have no information about state proximity to goals. Key characteristics:

- No evaluation of how close states are to goals
- Must systematically explore state space
- Example: Agent in Arad seeking Bucharest without geographic knowledge

#### Breadth-First Search (BFS)

Core characteristics:
- Expands nodes level by level
- Uses FIFO queue for frontier
- Complete even for infinite state spaces
- Optimal when all actions have same cost

Implementation details:
- Uses set of reached states for efficiency
- Performs early goal testing
- Simpler than general best-first search
- FIFO queue preferable to priority queue

Performance analysis:
- Time and space complexity: O(b^d)
    - b: branching factor
    - d: solution depth
- Memory is primary limitation
- Example metrics (b=10):
    - Depth 10: ~3 hours, 10TB memory
    - Depth 14: 3.5 years processing time

#### Uniform-Cost Search
- Variant of best-first search
- Uses path cost as evaluation function
- Implemented as `BEST-FIRST-SEARCH(problem, PATH-COST)`

#### Uniform Cost Search Characteristics

Key features:
- Extends BFS by considering action costs
- Expands nodes with lowest path cost first
- Implemented as best-first search using path cost
- Spreads in waves of uniform cost (not depth)

Example walkthrough:
1. Starts at initial node (e.g., Sibiu)
2. Expands lowest-cost successor first
3. Maintains cumulative path costs
4. Returns first path reaching goal

Performance metrics:
- Complete: Yes (if action costs > 0)
- Cost-optimal: Yes
- Time/space complexity: O(b^(1 + C*/ε))
    - C* = optimal solution cost
    - ε = minimum action cost
    - b = branching factor

Trade-offs:
- More optimal than BFS for varied costs
- May explore many low-cost paths before finding goal
- Higher complexity than BFS for equal costs
- Memory requirements can be significant
#### Depth-First Search (DFS)

Key characteristics:
- Expands deepest node in frontier first
- Usually implemented as tree-like search
- Does not maintain reached states table
- Backs up when reaching nodes without successors

Performance analysis:
- Not cost-optimal
- Complete for finite state spaces
- May loop infinitely in cyclic spaces
- Memory complexity: O(bm)
    - b: branching factor
    - m: maximum depth

Advantages:
- Much lower memory requirements than BFS
- Practical for tree-like search problems
- Core algorithm for many AI applications
    - Constraint satisfaction
    - Propositional satisfiability
    - Logic programming

#### Backtracking Search

A memory-efficient DFS variant:
- Generates one successor at a time
- Modifies current state directly
- Memory needs: O(m) for action path
- Requires reversible actions
- Can efficiently check for cycles
- Critical for problems with large state descriptions
#### Depth-Limited Search (DLS)
- Modified DFS with depth limit ℓ
- Treats nodes at depth ℓ as having no successors
- Time complexity: O(bℓ)
- Space complexity: O(bℓ)
- Incomplete if ℓ less than solution depth
- Can detect cycles by checking parent chain

#### Iterative Deepening Search (IDS)
- Combines benefits of DFS and BFS
- Tries increasing depth limits (0, 1, 2, ...)
- Memory requirements: O(bd) with solution, O(bm) without
- Complete and optimal for uniform action costs
- Time complexity: O(bd)

Key advantages:
- Memory-efficient like DFS
- Complete like BFS
- Optimal for uniform costs
- Good for unknown solution depths

Performance analysis:
- Appears wasteful but efficient in practice
- Most nodes are in bottom level
- Bottom level (d): generated once
- Level d-1: generated twice
- Root children: generated d times

Example comparison (b=10, d=5):
- IDS: 123,450 node generations
- BFS: 111,110 node generations

Hybrid approach:
- Run BFS until memory nearly full
- Switch to IDS from frontier nodes
- Best choice for large state spaces
- Used when solution depth unknown

### Bidirectional Search

A search strategy that:
- Searches forward from initial state and backward from goal state simultaneously
- Significantly reduces search space compared to unidirectional search
- Solution found when forward and backward searches meet

#### Implementation Details
- Maintains two frontiers and two reached state tables
- Expands node with minimum evaluation function from either frontier
- Forward and backward problems must be defined
- Requires reverse state transition capabilities
- First solution may not be optimal (depends on evaluation function)

#### Bidirectional Uniform-Cost Search
- Uses path cost as evaluation function
- Only expands nodes with cost <= C*/2 (optimal path cost)
- First solution found is guaranteed optimal
- Significant performance improvement over unidirectional search

#### Performance Benefits
- Search space reduction: bd/2 + bd/2 vs bd
- Example (b=10, d=10):
    - Unidirectional: 10^10 nodes
    - Bidirectional: 2 * 10^5 nodes
    - ~50,000x improvement

#### Termination
- Algorithm tracks best solution found
- Continues until no better solution possible
- May require multiple solution updates
- Termination test varies by evaluation function

### Comparing Uninformed Search Algorithms

Key comparison points across algorithms:

#### Breadth-First Search
- Complete (if b is finite)
- Cost-optimal for uniform costs
- Time & Space: O(bd)

#### Uniform-Cost Search
- Complete (if action costs ≥ ǫ > 0)
- Always cost-optimal
- Time & Space: O(b^(1+⌊C*/ǫ⌋))

#### Depth-First Search
- Not complete for tree search
- Not cost-optimal
- Time: O(bm)
- Space: O(bm)

#### Depth-Limited Search
- Not complete
- Not cost-optimal
- Time & Space: O(bℓ)

#### Iterative Deepening
- Complete (if b is finite)
- Cost-optimal for uniform costs
- Time: O(bd)
- Space: O(bd)

#### Bidirectional Search
- Complete (if b finite)
- Cost-optimal (for BFS/uniform-cost)
- Time & Space: O(b^(d/2))

Notes:
- b = branching factor
- d = shallowest solution depth
- m = maximum depth
- ℓ = depth limit
- C* = optimal path cost
- ǫ = minimum action cost

