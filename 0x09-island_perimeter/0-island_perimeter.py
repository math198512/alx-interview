#!/usr/bin/python3
"""Island perimeter computing module.
"""


def island_perimeter(grid):
    """Computes the perimeter of an island with no lakes.
    """
    row_length = len(grid)
    column_length = len(grid[0])

    perimeter = 0
    Connections = 0

    for i in range(row_length):
        for j in range(column_length):
            if grid[i][j] == 1:
                perimeter += 4

                if i != 0 and grid[i - 1][j] == 1:
                    Connections += 1
                if j != 0 and grid[i][j - 1] == 1:
                    Connections += 1
    return perimeter - Connections*2
