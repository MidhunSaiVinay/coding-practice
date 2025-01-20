# Binary Heap
## Priority Queue
A priority queue is a specialized data structure that implements a subset of the set interface. It maintains elements with associated priorities and supports these key operations:

- `build`: Constructs a heap from an array of elements
- `insert`: Adds a new element while maintaining heap properties
- `delete_max`: Removes and returns the highest priority element
- `find_max`: Returns the highest priority element without removing it

Priority queues are commonly used in:
- Task scheduling
- Event-driven simulations
- Dijkstra's shortest path algorithm

## Binary Heap Implementation
A binary heap is an efficient implementation of a priority queue that uses:
- A complete binary tree structure
- Heap property (max-heap or min-heap)
- Array-based storage for efficiency

## Priority Sort (Heap Sort)
Heap sort uses a binary heap to sort elements by:
1. Building a max-heap from input
2. Repeatedly extracting maximum
3. Time complexity: O(n log n)
