from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """Finds the element that appears only once in an array.

        Every other element appears exactly three times.

        Args:
            nums: A list of integers.

        Returns:
            The integer that appears only once.
        """
        ones = 0
        twos = 0
        
        for num in nums:
            # 1. Update 'twos' only if the bit is already in 'ones'
            twos |= (ones & num)
            
            # 2. Update 'ones' (standard XOR)
            ones ^= num
            
            # 3. If a bit is in both 'ones' and 'twos', it has appeared 3 times
            # Create a mask for bits that have NOT appeared 3 times
            three_mask = ~(ones & twos)
            
            # 4. Clear the bits that reached the 3rd appearance
            ones &= three_mask
            twos &= three_mask
            
        return ones