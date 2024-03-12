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

def solver(grid, row, column):

    if column==4:
        if row==3:
            return True
        row= row+1
        column =0

    if grid[row][column]>0:
        return solver( grid, row,column +1)
    
    for num in range(1,5):
        if is_validmove(grid, row, column,num):
            grid[row][column]=num

            if solver(grid, row,column+1):
                return True
            
        grid[row][column]=0

    return False

