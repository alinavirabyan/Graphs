# Dungeon Game

This project demonstrates the solution to the **Dungeon Game** problem using Dynamic Programming. The objective is to find the minimum initial health required for a knight to rescue a princess in a dungeon grid, starting from the top-left corner and reaching the bottom-right corner, ensuring the knight's health never drops to 0 or below.

## How It Works

1. Create a 2D dynamic programming table (`dp`) of the same dimensions as the grid.
2. Start from the bottom-right corner (destination) and set the minimum health required at that final cell.
3. Calculate the required health for the bottom row and the rightmost column moving backward.
4. For all other cells, select the minimum health needed between moving right or down, and subtract the cell's value.
5. Apply `max(1, ...)` at each step to ensure health never falls to 0 or below.
6. The top-left cell (`dp[0][0]`) stores the minimum initial health required to start the journey.

## Example

For the given grid:

```python
grid = [
    [-2, -3, 3],
    [-5, -10, 1],
    [10, 30, -5]
]

```

The algorithm calculates that the minimum initial health required to survive the path is `7`.

## Complexity

* **Time Complexity:** O(M × N)
* **Space Complexity:** O(M × N)

Where M is the number of rows and N is the number of columns in the grid.

## Main Concept

Dynamic Programming — 2D Grid Traversal / Minimum Health Path

## File

[`dungeon.py`](https://github.com/alinavirabyan/Graphs/blob/main/DungeonProblem/dungeon.py) — Implementation of the Dungeon Game algorithm.
