from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """Determines if the last index is reachable from the first.

        Args:
            nums: A list of non-negative integers representing max jump lengths.

        Returns:
            True if the last index is reachable, False otherwise.
        """
        farthest = 0
        n = len(nums)
        
        for i in range(n):
            # If current index is unreachable, we can't proceed
            if i > farthest:
                return False
            
            # Update the farthest index we can reach
            farthest = max(farthest, i + nums[i])
            
            # Optimization: if we can already reach the end, stop early
            if farthest >= n - 1:
                return True
                
        return farthest >= n - 1