from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        """Calculates the minimum path sum from top to bottom of the triangle.

        This implementation uses a bottom-up DP approach in-place.

        Args:
            triangle: A list of lists representing the triangle.

        Returns:
            The minimum path sum as an integer.
        """
        # Start from the second to last row and move upwards
        for row in range(len(triangle) - 2, -1, -1):
            for col in range(len(triangle[row])):
                # The minimum path sum for the current node is its value
                # plus the minimum of its two adjacent children below.
                lower_left = triangle[row + 1][col]
                lower_right = triangle[row + 1][col + 1]
                
                triangle[row][col] += min(lower_left, lower_right)
        
        # The top element now stores the total minimum path sum
        return triangle[0][0]