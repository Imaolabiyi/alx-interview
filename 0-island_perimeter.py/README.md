0x09. Island Perimeter
Introduction
This project involves solving the Island Perimeter problem, where we are given a 2D grid representing a map of water and land. The goal is to calculate the perimeter of a single island in the grid.

Water is represented by 0s.
Land is represented by 1s.
The grid is completely surrounded by water, and there is only one island with no internal lakes.
Problem Statement
You are given a grid of integers where:

0 represents water.
1 represents land.
Each cell is square, with a side length of 1. Cells are connected horizontally/vertically (not diagonally). The grid is rectangular, with its width and height not exceeding 100.

Write a function def island_perimeter(grid): that returns the perimeter of the island described in grid.

Example:
Given the following grid:

python
Copy code
grid = [
    [0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0]
]
The function should return 12, as the island's perimeter is 12.

Approach
The solution involves iterating over the grid and for each land cell (1), checking its four neighbors (up, down, left, right). Each time a neighboring cell is water (0) or out of bounds, we increment the perimeter by 1.

Key Concepts:
2D Array Traversal: Loop through each cell in the grid.
Boundary Checking: For each land cell, check if any of the four neighboring cells is either water or outside the grid.
Conditionally Add to Perimeter: If a neighboring cell is water or out of bounds, increase the perimeter count.
Algorithm
For each land cell (1):

Check its top, bottom, left, and right cells.
If the neighboring cell is water (0) or out of bounds, it contributes to the perimeter.
Code Implementation
python
Copy code
def island_perimeter(grid):
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Check all four directions
                if i == 0 or grid[i - 1][j] == 0:  # Up
                    perimeter += 1
                if i == rows - 1 or grid[i + 1][j] == 0:  # Down
                    perimeter += 1
                if j == 0 or grid[i][j - 1] == 0:  # Left
                    perimeter += 1
                if j == cols - 1 or grid[i][j + 1] == 0:  # Right
                    perimeter += 1

    return perimeter
Time Complexity:
The algorithm runs in O(n * m), where n is the number of rows and m is the number of columns in the grid. This ensures we visit every cell exactly once and check its neighbors.
Requirements
Python 3.4.3 or higher.
No external modules are allowed to be imported.
Project Specifications:
Allowed editors: vi, vim, emacs.
All files are executed/compiled on Ubuntu 20.04 LTS using python3.
Code must follow the PEP 8 style guide.
Author: Ima-obong Olabiyi
This project is part of the ALX Interview Preparation series.
