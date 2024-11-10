#!/usr/bin/python3
"""algorithm to solve N Queens problem"""

import sys


def is_safe(board, i, j, placed_queens):
    return not any(
                    i == i_
                    or j == j_
                    or abs(i - i_) == abs(j - j_) for i_, j_ in placed_queens)


def rec(board, i, placed_queens=None):
    n = len(board)
    if i == n and placed_queens is not None:
        print(placed_queens)

    if placed_queens is None:
        placed_queens = []
    for j in range(n):
        if is_safe(board, i, j, placed_queens):
            board[i][j] = 1
            placed_queens.append([i, j])
            rec(board, i+1, placed_queens[:])
            placed_queens.pop()
            board[i][j] = 0


def n_queens(n):
    board = [[0]*n for _ in range(n)]
    rec(board, 0)


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)
try:
    n = int(sys.argv[1])
except Exception:
    print("N must be a number")
    sys.exit(1)
if n < 4:
    print("N must be at least 4")
    sys.exit(1)
n_queens(n)
