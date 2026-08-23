# Longest Path in a Directed Acyclic Graph (DAG)

This project demonstrates how to find the longest paths from a starting vertex to all other reachable vertices in a Directed Acyclic Graph (DAG) with weighted edges. The algorithm leverages topological sorting with dynamic programming to update distances in linear time.

## How It Works

1. Perform a Topological Sort on the DAG using Depth-First Search (DFS) to obtain a valid linear ordering of vertices.
2. Initialize a distance dictionary `dist` with negative infinity (`-inf`) for all nodes, and set `dist[start] = 0` for the starting vertex.
3. Process vertices one by one in topological order.
4. For each reachable node, inspect all of its outgoing edges $(u, v)$ with weight $w$.
5. Relax the edges by updating `dist[v] = max(dist[v], dist[u] + w)` whenever a longer path is found.
6. Return the dictionary containing the maximum path lengths from the starting vertex to every node.

## Example

For the given directed acyclic graph:

```python
graph = {
    0: [(1, 5), (2, 3)],
    1: [(3, 6)],
    2: [(3, 7)],
    3: [(4, 2)],
    4: []
}
start_node = 0

```

The algorithm calculates the longest distances starting from node `0` to every reachable vertex and outputs:
`{0: 0, 1: 5, 2: 3, 3: 10, 4: 12}`

## Complexity

* **Time Complexity:** $O(V + E)$
* **Space Complexity:** $O(V + E)$

Where $V$ is the number of vertices and $E$ is the number of edges in the graph.

## Main Concept

Graph Algorithm — Longest Path in DAG using Topological Sort

## File

[`longest_path_dag.py`](https://github.com/alinavirabyan/Graphs/blob/main/LongestPathDAG/longest_path_dag.py) — Implementation of the Longest Path in DAG algorithm.
