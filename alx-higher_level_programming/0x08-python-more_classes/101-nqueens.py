#!/usr/bin/python3
"""A pyhton module that defines N queens problem"""


class ChessBoard:
    """A chess board for N queens problem"""
    def __init__(self, n):
        """Initialize ChessBoard class.

        Args:
            n (int): Size of the board
        """
        self.n = n
        self.board = [[0 for _ in range(n)] for _ in range(n)]
        self.solutions = []

    def __str__(self):
        """Prints the board"""
        return '\n'.join(' '.join(str(cell) for cell in row)
                         for row in self.board)

    def is_safe(self, row, col):
        """Checks if a position is safe from attack.

        Args:
            row (int): row position
            col (int): column position

        Returns:
            bool: True if safe, False otherwise
        """
        # Check this row on left side
        for i in range(col):
            if self.board[row][i] == 1:
                return False

        # Check upper diagonal on left side
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if self.board[i][j] == 1:
                return False

        # Check lower diagonal on left side
        for i, j in zip(range(row, self.n), range(col, -1, -1)):
            if self.board[i][j] == 1:
                return False

        return True

    def solve(self, col):
        """Solves the N queens problem.

        Args:
            col (int): column position
        """
        if col >= self.n:
            solution = []
            for i in range(self.n):
                for j in range(self.n):
                    if self.board[i][j] == 1:
                        solution.append([i, j])
            self.solutions.append(solution)
            return

        # Consider this column and try placing
        for row in range(self.n):
            if self.is_safe(row, col):
                self.board[row][col] = 1
                self.solve(col + 1)
                self.board[row][col] = 0

    def solveNQ(self):
        """Solves the N queens problem."""
        self.solve(0)
        return self.solutions


if __name__ == "__main__":
    import sys

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

    chessboard = ChessBoard(n)
    solutions = chessboard.solveNQ()

    if len(solutions) > 0:
        for solution in solutions:
            print(solution)
    else:
        print("No solutions found.")
