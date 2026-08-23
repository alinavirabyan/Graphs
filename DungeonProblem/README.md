# Dungeon Problem

This project demonstrates the **Dungeon Problem algorithm** for finding the minimum initial health needed to reach the bottom-right cell of a dungeon while keeping the health above `0`.

The algorithm uses **Dynamic Programming (DP)** to calculate the minimum health required at each cell.

## How It Works

1. Create a DP table with the same dimensions as the dungeon.
2. Start from the bottom-right cell.
3. Calculate the minimum health required to survive the last cell.
4. Fill the last row from right to left.
5. Fill the last column from bottom to top.
6. For every remaining cell, choose the smaller health requirement from moving **right** or **down**.
7. Subtract the current cell's value from the required health.
8. Make sure the required health is always at least `1`.
9. Return the minimum initial health required at the starting cell.

## Example

For the dungeon:

```text
[
    [-2, -3,  3],
    [-5, -10, 1],
    [10, 30, -5]
]
