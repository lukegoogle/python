from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """Determines if a word exists in a 2D grid.

        Args:
            board: A list of lists of strings representing the character grid.
            word: The string to search for within the grid.

        Returns:
            True if the word exists in the grid, False otherwise.
        """
        rows, cols = len(board), len(board[0])
        
        def dfs(r: int, c: int, index: int) -> bool:
            """Explores the grid using DFS to find the word suffix.

            Args:
                r: Current row index.
                c: Current column index.
                index: Current character index in the word we are looking for.

            Returns:
                True if the suffix starting at word[index] is found.
            """
            # Base case: all characters found
            if index == len(word):
                return True
            
            # Boundary and mismatch checks
            if (r < 0 or c < 0 or 
                r >= rows or c >= cols or 
                board[r][c] != word[index]):
                return False
            
            # Action: Mark the current cell as visited
            temp = board[r][c]
            board[r][c] = "#"
            
            # Recursion: Check all 4 directions
            found = (dfs(r + 1, c, index + 1) or
                     dfs(r - 1, c, index + 1) or
                     dfs(r, c + 1, index + 1) or
                     dfs(r, c - 1, index + 1))
            
            # Backtrack: Restore the cell for other paths
            board[r][c] = temp
            
            return found

        # Try starting DFS from every cell in the grid
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0] and dfs(r, c, 0):
                    return True
        
        return False