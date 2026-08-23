# Floyd-Warshall Algorithm

This project demonstrates the Floyd-Warshall algorithm for finding the shortest paths between all pairs of vertices in a weighted graph. The algorithm uses dynamic programming to iteratively update distance matrices by checking if passing through an intermediate vertex yields a shorter path and logs each distance update step.

## How It Works

1. Read the number of vertices ($V$) and edges ($E$) from user input to build an undirected weighted graph using 1-based indexing.
2. Initialize a $V \times V$ distance matrix with infinity (`inf`) for all pairs.
3. Populate the matrix with direct edge weights and set the diagonal distances (from each vertex to itself) to `0`.
4. Iterate through each vertex $k$ as an intermediate node.
5. For every pair of vertices $(i, j)$, check if the path passing through $k$ (`matrix[i][k] + matrix[k][j]`) is shorter than the direct distance `matrix[i][j]`.
6. Update `matrix[i][j]` whenever a shorter path is found and print a message logging the updated distance (`Թարմացվեց i -> j = weight`).

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

When running the algorithm, the system prints updates whenever a shorter path is discovered through intermediate nodes:

```text
Թարմացվեց 1 -> 3 = 6
Թարմացվեց 3 -> 1 = 6

```

## Complexity

* **Time Complexity:** $O(V^3)$
* **Space Complexity:** $O(V^2)$

Where $V$ is the number of vertices in the graph.

## Main Concept

Graph Algorithm — All-Pairs Shortest Path with Floyd-Warshall Algorithm

## File

[`floyd_warshall.py`](https://github.com/alinavirabyan/Graphs/blob/main/FloydWarshall/floyd_warshall.py) — Implementation of the Floyd-Warshall algorithm.
