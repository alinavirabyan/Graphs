# Kahn's Algorithm for Topological Sort

This project demonstrates Kahn's Algorithm for performing a Topological Sort on a Directed Acyclic Graph (DAG). Topological sorting produces a linear ordering of vertices such that for every directed edge $u \to v$, vertex $u$ comes before vertex $v$.

## How It Works

1. Calculate the in-degree (number of incoming edges) for each node in the graph.
2. Initialize a queue and enqueue all nodes with an in-degree of `0`.
3. Process nodes from the queue one by one:
* Remove a node from the queue and add it to the topological sort result list.
* For each neighbor of the removed node, decrement its in-degree by `1`.
* If a neighbor's in-degree becomes `0`, add it to the queue.


4. Repeat the process until the queue is empty.
5. If the topological sort list contains all nodes in the graph, return the valid topological order. Otherwise, return `"Cycle detected"` as the graph contains a directed cycle.

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

The algorithm calculates the topological order and outputs:
`[5, 4, 2, 0, 1, 3]`

*(Note: Topological sort orderings are not unique; other valid orderings may exist depending on traversal order.)*

## Complexity

* **Time Complexity:** $O(V + E)$
* **Space Complexity:** $O(V + E)$

Where $V$ is the number of vertices and $E$ is the number of edges in the graph.

## Main Concept

Graph Algorithm — Topological Sorting with Kahn's Algorithm (BFS)

## File

[`kahn_topological_sort.py`](http://github.com/alinavirabyan/Graphs/blob/main/KahnsAlgorithm/kahn_topological_sort.py) — Implementation of Kahn's Algorithm for Topological Sort.
