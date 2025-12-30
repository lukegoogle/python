from typing import List

class Solution:
    def grayCode(self, n: int) -> List[int]:
        """Generates an n-bit gray code sequence.

        Args:
            n: The number of bits in the gray code.

        Returns:
            A list of integers representing the gray code sequence.
        """
        # Start with the base case for 0 bits
        result = [0]
        
        for i in range(n):
            # Calculate the bit to be added (2^i)
            bit_to_add = 1 << i
            
            # Iterate backwards through the current result to mirror it
            # and add the high bit to the mirrored values.
            for j in range(len(result) - 1, -1, -1):
                result.append(result[j] | bit_to_add)
                
        return result