class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """Calculates the number of unique paths from top-left to bottom-right.

        Args:
            m: The number of rows in the grid.
            n: The number of columns in the grid.

        Returns:
            The total number of unique paths.
        """
        # Initialize a 2D DP table with 1s
        # (The first row and first column stay 1)
        dp = [[1] * n for _ in range(m)]
        
        # Start from (1, 1) and fill the table
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
                
        return dp[m-1][n-1]