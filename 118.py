from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        """Generates the first numRows of Pascal's Triangle.

        Args:
            numRows: The number of rows to generate.

        Returns:
            A list of lists representing Pascal's Triangle.
        """
        if numRows == 0:
            return []
        
        # Initialize the triangle with the first row
        triangle = [[1]]
        
        for i in range(1, numRows):
            # Start the current row with 1
            row = [1]
            # Reference to the previous row
            prev_row = triangle[i-1]
            
            # Each triangle element is equal to the sum of the elements 
            # above-and-to-the-left and above-and-to-the-right.
            for j in range(1, i):
                row.append(prev_row[j-1] + prev_row[j])
            
            # End the current row with 1
            row.append(1)
            triangle.append(row)
            
        return triangle