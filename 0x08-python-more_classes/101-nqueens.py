#!/usr/bin/python3
"""nqueens module"""

import sys


def init_board(n):
    """init of board"""
    board = []
    [board.append([]) for j in range(n)]
    [row.append(' ') for x in range(n) for row in board]
    return (board)


def board_copy(board):
    if isinstance(board, list):
        return list(map(board_copy, board))
    return (board)


def board_solution(board):
    solutions = []
    for r in range(len(board)):
        for c in range(len(board)):
            if board[r][c] == "Q":
                solutions.append([r, c])
                break
    return (solutions)


def output(board, row, col):
    for c in range(col + 1, len(board)):
        board[row][c] = "x"

    for c in range(col - 1, -1, -1):
        board[row][c] = "x"

    for r in range(row + 1, len(board)):
        board[r][col] = "x"

    for r in range(row - 1, -1, -1):
        board[r][col] = "x"

    c = col + 1
    for r in range(row + 1, len(board)):
        if c >= len(board):
            break
        board[r][c] = "x"
        c += 1

    c = col - 1
    for r in range(row - 1, -1, -1):
        if c < 0:
            break
        board[r][c]
        c -= 1

    c = col + 1
    for r in range(row - 1, -1, -1):
        if c >= len(board):
            break
        board[r][c] = "x"
        c += 1

    c = col - 1
    for r in range(row + 1, len(board)):
        if c < 0:
            break
        board[r][c] = "x"
        c -= 1


def solver(board, row, queens, solutions):
    if queens == len(board):
        solutions.append(board_solution(board))
        return (solutions)

    for c in range(len(board)):
        if board[row][c] == " ":
            temp_board = board_copy(board)
            temp_board[row][c] = "Q"
            output(temp_board, row, c)
            solutions = solver(temp_board, row + 1, queens + 1, solutions)
    return (solutions)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = init_board(int(sys.argv[1]))
    solutions = solver(board, 0, 0, [])
    for sol in solutions:
        print(sol)
