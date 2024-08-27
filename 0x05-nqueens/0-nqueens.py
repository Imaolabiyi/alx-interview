#!/usr/bin/python3
import sys

def is_valid(board, row, col):
    """Check if a queen can be placed on board[row][col]."""
    for i in range(row):
        if board[i][1] == col or \
           board[i][1] - board[i][0] == col - row or \
           board[i][1] + board[i][0] == col + row:
            return False
    return True

def solve_nqueens(n):
    """Solve the N-Queens problem and return all possible solutions."""
    def backtrack(row):
        if row == n:
            solutions.append([list(map(list, board))])
            return
        for col in range(n):
            if is_valid(board, row, col):
                board[row] = [row, col]
                backtrack(row + 1)
                board[row] = [-1, -1]
    
    solutions = []
    board = [[-1, -1] for _ in range(n)]
    backtrack(0)
    return solutions

def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_nqueens(n)
    for solution in solutions:
        print(solution)

if __name__ == "__main__":
    main()

