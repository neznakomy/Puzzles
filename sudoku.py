#
#    Project 10 - SUDOKU SOLVER
#
import os
from sudoku_board import example_board

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def greeting():
    print('\nWelcome to the Sudoku solver')
    print('\nIn this first iteration of Sudoku solver, you will need to populate')
    print('the file SUDOKU_BOARD.PY with your grid before running the program.\n')

def find_next_empty(puzzle):
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:   # is the location empty?
                return r, c
    return None, None                # no empty spaces left

def is_valid(puzzle, guess, row, col):
    #check complete rows and columns
    row_vals = puzzle[row]
    if guess in row_vals:            # this number already exists in the row
        return False
    col_vals = [puzzle[i][col]for i in range(9)]
    if guess in col_vals:            # this number already exists in the column
        return False
    # check the nine 'inner' square
    row_start = (row // 3) * 3
    col_start = (col // 3) * 3
    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False
    return True

def solve_puzzle(puzzle):
    row, col = find_next_empty(puzzle)
    if row is None:
        return True                  # we are done here - puzzled solved
    for guess in range(1,10):        # use only the numbers between 1-9
        if is_valid(puzzle, guess, row, col):
            puzzle[row][col] = guess
            if solve_puzzle(puzzle):
                return True
        puzzle[row][col] = -1        # it did not work out so reset the location
    return False

if __name__ == '__main__':
    cls()
    greeting()
    # show the initial board
    for l in example_board:
        print(l)
    print('\nSolving this puzzle...note that populated squares are 1-9, spaces are -1\n')
    # solve and display
    if solve_puzzle(example_board) is True:
        print('\nSolved this puzzle as below!\n')
    else:
        print('\nNot able to solve this puzzle - please check SUDOKU_BOARD.PY for errors\n')
    for l in example_board:
        print(l)
