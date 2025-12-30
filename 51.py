from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        """Finds all distinct solutions to the N-Queens puzzle.

        Args:
            n: The number of queens and the size of the board.

        Returns:
            A list of all valid board configurations.
        """
        res = []
        board = [["."] * n for _ in range(n)]

        # Tracking sets for O(1) lookups
        cols = set()
        pos_diag = set()  # (r + c)
        neg_diag = set()  # (r - c)

        def backtrack(r: int):
            # Base case: all rows filled
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return

            for c in range(n):
                # Check if the position is under attack
                if c in cols or (r + c) in pos_diag or (r - c) in neg_diag:
                    continue

                # "Choose" - Place the queen
                cols.add(c)
                pos_diag.add(r + c)
                neg_diag.add(r - c)
                board[r][c] = "Q"

                # "Explore" - Move to the next row
                backtrack(r + 1)

                # "Backtrack" - Remove the queen
                cols.remove(c)
                pos_diag.remove(r + c)
                neg_diag.remove(r - c)
                board[r][c] = "."

        backtrack(0)
        return res