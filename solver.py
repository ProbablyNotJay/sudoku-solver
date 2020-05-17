# A program to solve Sudoku problems
# First version uses a backtracking algorithm

def print_puzzle(array):
    grid = ["-----------------"]

    for row in array:
        grid.append(' '.join(str(x) for x in row))
    grid.append("-----------------")
    print('\n'.join(grid))
    print("0's are blank spaces")

puzzle = [[0 for x in range(9)]for y in range(9)]
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
