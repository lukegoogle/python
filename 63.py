from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        """Calculates unique paths in a grid containing obstacles.

        Args:
            obstacleGrid: A 2D list where 1 represents an obstacle and 0 a path.

        Returns:
            The total number of unique paths from top-left to bottom-right.
        """
        if not obstacleGrid or obstacleGrid[0][0] == 1:
            return 0
            
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        
        # Initialize DP table
        dp = [[0] * n for _ in range(m)]
        
        # Starting point
        dp[0][0] = 1
        
        # Fill first column
        for i in range(1, m):
            dp[i][0] = dp[i-1][0] if obstacleGrid[i][0] == 0 else 0
            
        # Fill first row
        for j in range(1, n):
            dp[0][j] = dp[0][j-1] if obstacleGrid[0][j] == 0 else 0
            
        # Fill the rest of the grid
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
                    
        return dp[m-1][n-1]