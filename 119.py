from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        """Returns the k-th (0-indexed) row of Pascal's Triangle.

        This implementation uses O(k) space by updating a single list in-place.

        Args:
            rowIndex: The 0-based index of the row to retrieve.

        Returns:
            A list of integers representing the requested row.
        """
        # Initialize row with the 0-th row: [1]
        row = [1]
        
        for i in range(1, rowIndex + 1):
            # Append 1 to represent the last element of the current row
            row.append(1)
            
            # Update the middle elements backwards to avoid overwriting 
            # values needed for the current calculation.
            # We go from index (i-1) down to 1.
            for j in range(i - 1, 0, -1):
                row[j] = row[j] + row[j-1]
                
        return row