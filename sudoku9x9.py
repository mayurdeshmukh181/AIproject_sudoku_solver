size = 9
def solve_sudoku(grid):
    empty_cell = find_empty_cell(grid)
    if not empty_cell:
        # If no empty cells left, the puzzle is solved
        return True
    
    row, col = empty_cell
    
    for num in range(size):
        if is_valid_move(grid, row, col, num+1):
            grid[row][col] = num+1
            
            if solve_sudoku(grid):
                return True
            # Backtrack if the current placement doesn't lead to a solution
            grid[row][col] = 0
    
    # If no valid candidates for the current cell, trigger backtracking
    return False

def find_empty_cell(grid):
    for i in range(size):
        for j in range(size):
            if grid[i][j] == 0:
                return (i, j)
    return None

def is_valid_move(grid, row, col, num):
    # Check if 'num' is not already present in the same row, column, or subgrid
    return (not used_in_row(grid, row, num)
            and not used_in_col(grid, col, num)
            and not used_in_subgrid(grid, row - row % 3, col - col % 3, num))

def used_in_row(grid, row, num):
    return num in grid[row]

def used_in_col(grid, col, num):
    return any(row[col] == num for row in grid)

def used_in_subgrid(grid, start_row, start_col, num):
    for i in range(3):
        for j in range(3):
            if grid[i + start_row][j + start_col] == num:
                return True
    return False

def print_grid(grid):
    for row in grid:
        print(" ".join(map(str, row)))

sudoku_grid = [
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

if solve_sudoku(sudoku_grid):
        print("Sudoku puzzle solved successfully:")
        print_grid(sudoku_grid)
else:
        print("No solution exists for the given Sudoku puzzle.")
