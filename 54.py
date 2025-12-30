from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """Returns all elements of a matrix in spiral order.

        Args:
            matrix: A 2D list of integers.

        Returns:
            A list containing the elements in spiral order.
        """
        if not matrix:
            return []
            
        res = []
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        
        while top <= bottom and left <= right:
            # 1. Traverse Right
            for i in range(left, right + 1):
                res.append(matrix[top][i])
            top += 1
            
            # 2. Traverse Down
            for i in range(top, bottom + 1):
                res.append(matrix[i][right])
            right -= 1
            
            # 3. Traverse Left
            # Check condition again because top was incremented
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    res.append(matrix[bottom][i])
                bottom -= 1
            
            # 4. Traverse Up
            # Check condition again because right was decremented
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    res.append(matrix[i][left])
                left += 1
                
        return res