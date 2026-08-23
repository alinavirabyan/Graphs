# Breadth-First Search

This project demonstrates the **Breadth-First Search (BFS) algorithm** for traversing a graph.

BFS explores a graph level by level, starting from a selected node and visiting its neighboring nodes before moving to the next level.

## How It Works

1. Create a queue and add the starting node.
2. Mark the starting node as visited.
3. Remove the first node from the queue.
4. Print the current node.
5. Check its connected edges.
6. Add unvisited neighboring nodes to the queue.
7. Continue until the queue is empty.

## Example

For the graph:

```text
[[4, 3], [3, 1], [3, 8], [2, 8]]
```

The program asks for a starting node and performs a BFS traversal from that node.

## Complexity

* **Time Complexity:** O(V + E)
* **Space Complexity:** O(V)

Where `V` is the number of vertices and `E` is the number of edges.

## Main Concept

**Graph Traversal — Breadth-First Search (BFS)**

## File

* [`bfs.py`](https://github.com/alinavirabyan/Graphs/blob/main/BreadthFirstSearch/bfs.py) — Implementation of the Breadth-First Search algorithm.
