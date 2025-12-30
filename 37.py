from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """Solves the Sudoku puzzle in-place using backtracking.

        Args:
            board: A 2D list of strings representing the 9x9 Sudoku board.
        """
        self._solve(board)

    def _solve(self, board: List[List[str]]) -> bool:
        """Recursive helper to fill the board.

        Returns:
            True if the board is successfully solved, False otherwise.
        """
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    for char in "123456789":
                        if self._is_valid(board, r, c, char):
                            board[r][c] = char
                            
                            if self._solve(board):
                                return True
                            
                            # Backtrack: reset the cell
                            board[r][c] = "."
                    return False
        return True

    def _is_valid(self, board: List[List[str]], row: int, col: int, char: str) -> bool:
        """Checks if placing char at board[row][col] is valid."""
        for i in range(9):
            # Check row
            if board[row][i] == char:
                return False
            # Check column
            if board[i][col] == char:
                return False
            # Check 3x3 box
            box_r = 3 * (row // 3) + i // 3
            box_c = 3 * (col // 3) + i % 3
            if board[box_r][box_c] == char:
                return False
        return True