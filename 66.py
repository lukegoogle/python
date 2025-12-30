from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        """Increments a large integer represented as a list of digits by one.

        Args:
            digits: A list of integers representing the digits of a number.

        Returns:
            The list of digits after incrementing the number by one.
        """
        n = len(digits)
        
        # Traverse the list in reverse order
        for i in range(n - 1, -1, -1):
            if digits[i] < 9:
                # If the digit is not 9, increment and we are done
                digits[i] += 1
                return digits
            
            # If the digit is 9, it becomes 0 and carry continues
            digits[i] = 0
            
        # If we reach here, it means all digits were 9 (e.g., [9, 9, 9])
        # We need to prepend 1 to the result
        return [1] + digits