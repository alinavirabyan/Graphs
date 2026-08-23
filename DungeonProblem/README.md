````markdown
# Dungeon Problem

This project demonstrates the **Dungeon Problem algorithm** for finding the minimum initial health required to reach the bottom-right cell of a dungeon while keeping the health above `0`.

The algorithm uses **Dynamic Programming (DP)** to calculate the minimum health required at each cell.

## How It Works

1. Create a DP table with the same dimensions as the dungeon.
2. Start from the bottom-right cell.
3. Calculate the minimum health required to survive the destination cell.
4. Fill the last column from bottom to top.
5. Fill the last row from right to left.
6. For each remaining cell, check the minimum health required from moving down or right.
7. Choose the path that requires less health.
8. Subtract the current cell's value from the required health.
9. Make sure the required health is always at least `1`.
10. Return the value at `dp[0][0]`.

## Example

For the dungeon:

```text
[
    [-2, -3,  3],
    [-5, -10, 1],
    [10, 30, -5]
]
````

The minimum initial health required is:

```text
7
```

## Complexity

* **Time Complexity:** O(m × n)
* **Space Complexity:** O(m × n)

Where `m` is the number of rows and `n` is the number of columns.

## Main Concept

**Dynamic Programming — Grid-Based Problem**

## File

* [`dungeon.py`](https://github.com/alinavirabyan/Graphs/blob/main/DungeonProblem/dungeon.py) — Implementation of the Dungeon Problem algorithm.

