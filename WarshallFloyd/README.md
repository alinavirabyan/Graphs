# Floyd-Warshall Algorithm

This project demonstrates the Floyd-Warshall algorithm for finding the shortest paths between all pairs of vertices in a weighted graph. The algorithm uses dynamic programming to iteratively update distance matrices by checking if passing through an intermediate vertex yields a shorter path.

## How It Works

1. Read the number of vertices ($V$) and edges ($E$) to build an adjacency list representing an undirected graph.
2. Initialize a $V \times V$ distance matrix with infinity (`inf`) for all pairs.
3. Populate the matrix with edge weights and set the distance from each vertex to itself to `0` ($D^0$).
4. Iterate through each vertex $k$ as an intermediate node.
5. For every pair of vertices $(i, j)$, update `matrix[i][j]` if the path through intermediate vertex $k$ (`matrix[i][k] + matrix[k][j]`) is shorter than the direct path.
6. Print the distance matrix after considering each intermediate vertex ($D^1, D^2, \dots, D^V$).

## Example

For a graph with $3$ vertices and $3$ weighted edges:

```text
Vertices: 3
Edges: 3
Edges input (u, v, w):
1 2 4
2 3 2
1 3 10

```

The algorithm outputs the initial distance matrix $D^0$:

```python
[0, 4, 10]
[4, 0, 2]
[10, 2, 0]

```

After processing intermediate nodes, the final matrix $D^3$ contains the shortest path distances between all pairs of vertices:

```python
[0, 4, 6]
[4, 0, 2]
[6, 2, 0]

```

## Complexity

* **Time Complexity:** $O(V^3)$
* **Space Complexity:** $O(V^2)$

Where $V$ is the number of vertices in the graph.

## Main Concept

Graph Algorithm — All-Pairs Shortest Path with Floyd-Warshall Algorithm

## File

[`warshall_floyd.py`](https://github.com/alinavirabyan/Graphs/blob/main/WarshallFloyd/warshall_floyd.py) — Implementation of the Floyd-Warshall algorithm.
