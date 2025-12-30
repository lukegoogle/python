from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """Rotates an n x n 2D matrix 90 degrees clockwise in-place.

        Args:
            matrix: A square 2D list of integers.
        """
        n = len(matrix)
        
        # Step 1: Transpose the matrix
        # We only iterate over the upper triangle to avoid swapping twice
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # Step 2: Reflect (Reverse each row)
        for i in range(n):
            matrix[i].reverse()