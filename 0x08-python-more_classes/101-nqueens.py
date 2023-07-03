#!/usr/bin/python3

import sys

def is_safe(board, row, col):
    # Check if a queen can be placed at the given position
    for i in range(row):
        # Check if there is a queen in the same column
        if board[i] == col:
            return False
        # Check if there is a queen in the same diagonal
        if abs(board[i] - col) == abs(i - row):
            return False
    return True

def solve_nqueens(board, row, n):
    if row == n:
        # All queens are placed, print the solution
        print([[i, board[i]] for i in range(n)])
    else:
        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                solve_nqueens(board, row + 1, n)

def nqueens(n):
    if not isinstance(n, int):
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * n
    solve_nqueens(board, 0, n)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
        nqueens(n)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
