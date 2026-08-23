# Find Center of Star Graph

This project demonstrates an optimal $O(1)$ time algorithm to find the center vertex of a star graph. In a star graph with $N$ vertices, there is one central node connected to $N - 1$ outer nodes, meaning the center node must appear in every edge of the graph.

## How It Works

1. Take the first two edges from the edge list: `edges[0]` and `edges[1]`.
2. Extract the two nodes of the first edge, let's call them `a` and `b`.
3. Check if node `a` is present in the second edge (`edges[1]`).
4. If node `a` is in the second edge, then `a` is connected to multiple vertices and must be the center node.
5. Otherwise, node `b` is the center node.
6. Calculate total vertices as `len(edges) + 1` and total edges as `len(edges)`.

## Example

For the given star graph edges:

```python
edges = [[1, 8], [8, 4], [8, 5]]

```

The algorithm checks node `1` against the second edge `[8, 4]`. Since `1` is not present, it determines that `8` is the center vertex and outputs:

```text
center vertex:  8
vertex: 4
edg:  3

```

## Complexity

* **Time Complexity:** $O(1)$
* **Space Complexity:** $O(1)$

The center node is found by inspecting only the first two edges, requiring constant time and memory.

## Main Concept

Graph Algorithm — Star Graph Center Identification

## File

[`find_center.py`](https://github.com/alinavirabyan/Graphs/blob/main/FindCenter/find_center.py) — Implementation of the Star Graph Center finding algorithm.
