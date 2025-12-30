from typing import List

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        """Finds the largest rectangle containing only 1s in a binary matrix.

        Args:
            matrix: A list of lists of strings ('0' or '1').

        Returns:
            The area of the largest rectangle.
        """
        if not matrix or not matrix[0]:
            return 0
        
        cols = len(matrix[0])
        # heights array stores the histogram bar heights for the current row
        heights = [0] * (cols + 1)  # +1 for the sentinel 0
        max_area = 0
        
        for row in matrix:
            # Update heights for the current row
            for i in range(cols):
                if row[i] == '1':
                    heights[i] += 1
                else:
                    heights[i] = 0
            
            # Solve the Largest Rectangle in Histogram problem for this row
            stack = [-1]
            for i in range(len(heights)):
                while heights[i] < heights[stack[-1]]:
                    h = heights[stack.pop()]
                    w = i - stack[-1] - 1
                    max_area = max(max_area, h * w)
                stack.append(i)
                
        return max_area