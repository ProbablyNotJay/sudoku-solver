# A program to solve Sudoku problems
# First version uses a backtracking algorithm

def print_puzzle(array):
    grid = ["-----------------"]

    for row in array:
        grid.append(' '.join(str(x) for x in row))
    grid.append("-----------------")
    print('\n'.join(grid))

def find_blank(array, location):
    for row in range(9):
        for col in range(9):
            if(array[row][col]==0):
                location[0] = row
                location[1] = col
                return True
    return False

def check_if_valid(array, row, column, number):
    if(not used_in_row(array, row, number) and not used_in_column(array, column, number) and not used_in_subgrid(array, row - row%3, column - column%3, number)):
        return True
    return False

def used_in_column(array, column, number):
    for i in range(9):
        if(array[i][column] == number):
            return True
    return False

def used_in_row(array, row, number):
    for i in range(9):
        if(array[row][i] == number):
            return True
    return False

def used_in_subgrid(array, row, column, number):
    for i in range(3):
        for j in range(3):
            if(array[i + row][j + column] == number):
                return True
    return False

def solve_puzzle(array):
    location = [0, 0]

    if(not find_blank(array, location)):
        return True

    row = location[0]
    column = location[1]

    for number in range(1, 10):
        if(check_if_valid(array, row, column, number)):
            array[row][column] = number

            if(solve_puzzle(array)):
                return True

            array[row][column] = 0

    return False



puzzle = [[0 for x in range(9)]for y in range(9)]
print("0's are blank spaces")
puzzle = [[3,0,6,5,0,8,4,0,0],
          [5,2,0,0,0,0,0,0,0],
          [0,8,7,0,0,0,0,3,1],
          [0,0,3,0,1,0,0,8,0],
          [9,0,0,8,6,3,0,0,5],
          [0,5,0,0,9,0,6,0,0],
          [1,3,0,0,0,0,2,5,0],
          [0,0,0,0,0,0,0,7,4],
          [0,0,5,2,0,6,3,0,0]]
print_puzzle(puzzle)
print(" ")
print("Working")
print(" ")
if(solve_puzzle(puzzle)):
    print_puzzle(puzzle)
else:
    print("We've Fucked It Lads")
