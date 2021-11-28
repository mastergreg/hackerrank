#!/usr/bin/python3


def calculate_prod_4_horizontal(x, y, grid):
    try:
        return grid[x][y] * grid[x][y + 1] * grid[x][y + 2] * grid[x][y + 3]
    except:
        return 0


def calculate_prod_4_vertical(x, y, grid):
    try:
        return grid[x][y] * grid[x + 1][y] * grid[x + 2][y] * grid[x + 3][y]
    except:
        return 0


def calculate_prod_4_diagonal(x, y, grid):
    try:
        return grid[x][y] * grid[x + 1][y + 1] * grid[x + 2][y + 2] * grid[x + 3][y + 3]
    except:
        return 0


def calculate_prod_4_diagonal_cross(x, y, grid):
    try:
        return grid[x + 3][y] * grid[x + 2][y + 1] * grid[x + 1][y + 2] * grid[x][y + 3]
    except:
        return 0


def calculate_prod_4(x, y, grid):
    horiz = calculate_prod_4_horizontal(x, y, grid)
    vert = calculate_prod_4_vertical(x, y, grid)
    diag = calculate_prod_4_diagonal(x, y, grid)
    diagx = calculate_prod_4_diagonal_cross(x, y, grid)
    return max(horiz, vert, diag, diagx)


def solve(x):
    prod = 0
    for i in range(20):
        for j in range(20):
            prod = max(prod, calculate_prod_4(i, j, x))
    return prod


def main():
    grid = []
    for grid_i in range(20):
        grid_t = [int(grid_temp) for grid_temp in input().strip().split(" ")]
        grid.append(grid_t)
    s = solve(grid)
    print(s)


if __name__ == "__main__":
    main()
