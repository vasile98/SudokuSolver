# @todo function to find empty locations
# @todo functions to find if a number is used in a row column or box
# @todo implement the main solver function

# Find empty locations in the grid
# Given a grid find and empty location ,if it exist  save it in the object l and return true
# else return false
def empty_locations(grid, l):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                l[0] = i
                l[1] = j
                return True
    return False


# Given a grid a row and a number check if that numbers appears in that row
# If it appears return True else return False
def used_in_row(grid, row, nr):
    for j in range(9):
        if grid[row][j] == nr:
            return True
    return False


# Given a grid a column and a number check if that numbers appears in that column
# If it appears return True else return False
def used_in_column(grid, col, nr):
    for i in range(9):
        if grid[i][col] == nr:
            return True
    return False


# Given a grid a column a row and a number check if that numbers appears in his 3x3 box
# If it appears return True else return False
def used_in_box(grid, row, col, nr):
    # To find the row and column where the 3x3 box starts
    # we can subtract the rest of row % 3 from our row and col % 3 from our column
    row_box_start = row - row % 3
    col_box_start = col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[i + row_box_start][j + col_box_start] == nr:
                return True
    return False


# Check if a number can be assigned to a given row and column
# Return true if possible and false otherwise
def check_if_nr_ok(grid, row, col, nr):
    return not used_in_row(grid, row, nr) and not used_in_column(grid, col, nr) and not used_in_box(grid, row, col, nr)


# Given a partially filled sudoku grid try and solve it to meet all sudoku requirements Using a backtracking
# algorithm assign a number from 1 to 9 to an empty space check if assigning the number to current index makes the
# grid unsafe or not, if safe then recursively call the function for all safe cases from 0 to 9. if any recursive
# call returns true, end the loop and return true. If no recursive call returns true then return false.
def solve(grid):
    # a list to keep track of empty locations
    l = [0, 0]

    # If there is no empty location we are done
    if not empty_locations(grid, l):
        return True

    # Assigning list values to row and col
    # that we got from the above function
    row = l[0]
    col = l[1]

    # consider digits 1 to 9
    for nr in range(1, 10):

        # if this number can be assigned in this location
        if check_if_nr_ok(grid, row, col, nr):

            # make assignment
            grid[row][col] = nr

            # return, if success,
            if solve(grid):
                return True

            # failure, unmake & try again
            grid[row][col] = 0

    # this triggers backtracking
    return False


# Main functions to test
if __name__ == '__main__':
    # create a 9x9 grid for testing
    grid = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
            [5, 2, 0, 0, 0, 0, 0, 0, 0],
            [0, 8, 7, 0, 0, 0, 0, 3, 1],
            [0, 0, 3, 0, 1, 0, 0, 8, 0],
            [9, 0, 0, 8, 6, 3, 0, 0, 5],
            [0, 5, 0, 0, 9, 0, 6, 0, 0],
            [1, 3, 0, 0, 0, 0, 2, 5, 0],
            [0, 0, 0, 0, 0, 0, 0, 7, 4],
            [0, 0, 5, 2, 0, 6, 3, 0, 0]]

    l = [0, 0]
    # print(empty_locations(grid,l),l)
    if solve(grid):
        for i in range(9):
            for j in range(9):
                print(grid[i][j], end=' ')
            print(end='\n')
    else:
        print("No solution found")
