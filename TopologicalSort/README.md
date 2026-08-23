# Topological Sort (DFS-based)

This project demonstrates how to perform a Topological Sort on a Directed Acyclic Graph (DAG) using Depth-First Search (DFS). Topological sorting produces a linear ordering of vertices such that for every directed edge $u \to v$, vertex $u$ comes before vertex $v$.

## How It Works

1. Maintain a `visited` set to keep track of processed nodes and a `stack` to store the ordering.
2. Iterate through all nodes in the graph; if a node has not been visited, perform a Depth-First Search (DFS) starting from that node.
3. Recursively visit all unvisited neighbors of the current node.
4. After visiting all neighbors of a node, push the node onto the stack.
5. Once all nodes are processed, reverse the stack (`stack[::-1]`) to obtain the correct topological order.

## Example

For the given directed acyclic graph:

```python
graph = {
    5: [2, 0],
    4: [0, 1],
    2: [3],
    3: [],
    1: [3],
    0: []
}

```

The algorithm calculates the topological ordering and outputs:
`[5, 4, 2, 1, 3, 0]`

*(Note: Topological sort orderings are not unique; other valid orderings may exist depending on traversal order.)*

## Complexity

* **Time Complexity:** $O(V + E)$
* **Space Complexity:** $O(V + E)$

Where $V$ is the number of vertices and $E$ is the number of edges in the graph.

## Main Concept

Graph Algorithm — Topological Sorting with Depth-First Search (DFS)

## File

[`topological_sort.py`](https://github.com/alinavirabyan/Graphs/blob/main/TopologicalSort/topological_sort.py) — Implementation of the DFS-based Topological Sort algorithm.
