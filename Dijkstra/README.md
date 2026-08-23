# Dijkstra

This project demonstrates **Dijkstra's algorithm** for finding the shortest paths from a starting vertex to all reachable vertices in a weighted graph.

The algorithm uses a **Priority Queue (`heapq`)** to efficiently select the vertex with the smallest known distance.

## How It Works

1. Create a graph with vertices and weighted edges.
2. Set the distance of the starting vertex to `0` and all other distances to infinity.
3. Add the starting vertex to a priority queue.
4. Select the vertex with the smallest distance.
5. Check all of its neighboring vertices.
6. Update their distances if a shorter path is found.
7. Continue until all reachable vertices have been processed.
8. Print the shortest distance from the starting vertex to each vertex.

## Example

For a weighted graph, the algorithm calculates the shortest distance from the selected starting vertex to every reachable vertex.

If a vertex cannot be reached, the program reports it as **unreachable**.

## Complexity

- **Time Complexity:** O((V + E) log V)
- **Space Complexity:** O(V + E)

Where `V` is the number of vertices and `E` is the number of edges.

## Main Concept

**Graph Algorithm — Shortest Path with Dijkstra's Algorithm**

## File

- [`dijkstra.py`](https://github.com/alinavirabyan/Graphs/blob/main/Dijkstra/dijkstra.py) — Implementation of Dijkstra's shortest path algorithm.
