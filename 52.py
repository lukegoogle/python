class Solution:
    def totalNQueens(self, n: int) -> int:
        """Calculates the total number of distinct solutions to the N-Queens puzzle.

        Args:
            n: The number of queens and the size of the board.

        Returns:
            The total count of unique valid configurations.
        """
        self.count = 0
        cols = set()
        pos_diag = set()  # (r + c)
        neg_diag = set()  # (r - c)

        def backtrack(r: int):
            if r == n:
                self.count += 1
                return

            for c in range(n):
                if c in cols or (r + c) in pos_diag or (r - c) in neg_diag:
                    continue

                # Choose
                cols.add(c)
                pos_diag.add(r + c)
                neg_diag.add(r - c)

                # Explore
                backtrack(r + 1)

                # Backtrack
                cols.remove(c)
                pos_diag.remove(r + c)
                neg_diag.remove(r - c)

        backtrack(0)
        return self.count