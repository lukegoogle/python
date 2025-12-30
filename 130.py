from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """Modifies the board in-place to capture surrounded regions.
        
        A region is captured if it is not connected to the board boundary.

        Args:
            board: A 2D grid of 'X' and 'O' characters.
        """
        if not board or not board[0]:
            return

        rows, cols = len(board), len(board[0])

        def dfs(r: int, c: int):
            """Helper to mark boundary-connected 'O's as safe."""
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != 'O':
                return
            
            # Mark as safe
            board[r][c] = 'S'
            
            # Explore neighbors
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # Step 1: Start DFS from all 'O's on the border
        for r in range(rows):
            dfs(r, 0)
            dfs(r, cols - 1)
        
        for c in range(cols):
            dfs(0, c)
            dfs(rows - 1, c)

        # Step 2: Traverse the board to flip characters
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    # This was a surrounded 'O'
                    board[r][c] = 'X'
                elif board[r][c] == 'S':
                    # This was a safe 'O', restore it
                    board[r][c] = 'O'