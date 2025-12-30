from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        """Calculates the minimum path sum from top-left to bottom-right.

        Args:
            grid: A 2D list of non-negative integers.

        Returns:
            The minimum sum of all numbers along the path.
        """
        if not grid or not grid[0]:
            return 0
            
        m, n = len(grid), len(grid[0])
        
        # Initialize DP table (or modify grid in-place to save space)
        # Here we use the grid itself to achieve O(1) extra space
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                elif i == 0:
                    # First row: can only come from the left
                    grid[i][j] += grid[i][j-1]
                elif j == 0:
                    # First column: can only come from above
                    grid[i][j] += grid[i-1][j]
                else:
                    # General case: take the minimum of top or left
                    grid[i][j] += min(grid[i-1][j], grid[i][j-1])
                    
        return grid[m-1][n-1]