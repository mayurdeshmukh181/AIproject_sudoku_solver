def get_empty_locations(grid):
    empty_locations = []

    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:  # Found an empty cell
                legal_values = get_legal_values(grid, i, j)
                num_legal_values = len(legal_values)
                empty_locations.append(((i, j), legal_values, num_legal_values))

    # Sort the list of empty locations based on the number of legal values
    empty_locations.sort(key=lambda x: x[2])
    return empty_locations


def get_legal_values(grid, row, column):
    legal_values = set(range(1, 10))  # Initialize with all possible values

    # Check row and column
    for i in range(9):
        if grid[row][i] in legal_values:
            legal_values.remove(grid[row][i])
        if grid[i][column] in legal_values:
            legal_values.remove(grid[i][column])

    # Check 3x3 subgrid
    start_row = row - row % 3
    start_column = column - column % 3
    for i in range(3):
        for j in range(3):
            if grid[start_row + i][start_column + j] in legal_values:
                legal_values.remove(grid[start_row + i][start_column + j])

    return legal_values


def solver(grid):
    empty_locations = get_empty_locations(grid)
    if not empty_locations:  # If there are no empty cells, the puzzle is solved
        return True

    (row, column), legal_values, _ = empty_locations[0]  # Select the empty cell with the least number of legal values

    for num in legal_values:
        grid[row][column] = num

        if solver(grid):
            return True

        grid[row][column] = 0  # Backtrack if the current assignment does not lead to a solution

    return False


# Sudoku grid
grid = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

# Solve Sudoku
if solver(grid):
    for row in grid:
        print(row)
else:
    print("No solution exists for this sudoku")
