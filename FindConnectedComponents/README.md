# Connected Components in a Graph

This project demonstrates how to find all connected components in an undirected graph using Depth-First Search (DFS). A connected component is a maximal subgraph where every pair of vertices is connected to each other by a path.

## How It Works

1. Initialize an empty set `visited` to keep track of processed nodes and a list `components` to store each component.
2. Iterate through every node in the graph.
3. If a node has not been visited, start a Depth-First Search (DFS) from that node.
4. During DFS, traverse all reachable neighbors recursively and collect them into a set representing the current component.
5. Add the newly found component to the list of components and update the `visited` set with all its nodes.
6. Return the final list of connected components.

## Example

For the given graph:

```python
graph = {
    0: [1, 2],
    1: [0],
    2: [0],
    3: [4],
    4: [3],
    5: []
}

```

The algorithm finds 3 distinct connected components and outputs:
`[{0, 1, 2}, {3, 4}, {5}]`

## Complexity

* **Time Complexity:** O(V + E)
* **Space Complexity:** O(V + E)

Where V is the number of vertices and E is the number of edges in the graph.

## Main Concept

Graph Algorithm — Connected Components with Depth-First Search (DFS)

## File

[`connected_components.py`](https://github.com/alinavirabyan/Graphs/blob/main/Find%20connected%20components) — Implementation of the Connected Components algorithm.
