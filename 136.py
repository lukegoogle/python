from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """Finds the element that appears only once in an array of pairs.

        Args:
            nums: A list of integers where every element appears twice 
                except for one.

        Returns:
            The integer that appears only once.
        """
        result = 0
        for num in nums:
            # Applying XOR logic
            result ^= num
        return result