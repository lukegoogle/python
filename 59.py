from typing import List

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        """Generates an n x n matrix filled with numbers 1 to n^2 in spiral order.

        Args:
            n: The dimension of the square matrix.

        Returns:
            An n x n 2D list containing the spiral pattern.
        """
        # Initialize the matrix with zeros
        matrix = [[0] * n for _ in range(n)]
        
        top, bottom = 0, n - 1
        left, right = 0, n - 1
        num = 1
        
        while num <= n * n:
            # 1. Fill Right
            for i in range(left, right + 1):
                matrix[top][i] = num
                num += 1
            top += 1
            
            # 2. Fill Down
            for i in range(top, bottom + 1):
                matrix[i][right] = num
                num += 1
            right -= 1
            
            # 3. Fill Left
            for i in range(right, left - 1, -1):
                matrix[bottom][i] = num
                num += 1
            bottom -= 1
            
            # 4. Fill Up
            for i in range(bottom, top - 1, -1):
                matrix[i][left] = num
                num += 1
            left += 1
            
        return matrix