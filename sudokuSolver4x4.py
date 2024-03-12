def is_validmove(grid,row,column,number):
    for x in range(4):
        if grid[row][x] == number:
            return False
    
    for x in range(4):
        if grid[x][column] == number:
            return False
        
    corner_row=row-row%2
    corner_column= column-column%2
    for x in range(2):
        for y in range(2):
            if grid[corner_row+x][corner_column+y] == number:
                return False
    
    return True
