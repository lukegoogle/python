from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """Finds the contiguous subarray with the largest sum using Kadane's Algorithm.

        Args:
            nums: A list of integers.

        Returns:
            The maximum sum of a contiguous subarray.
        """
        # Initialize both with the first element
        max_sum = nums[0]
        current_sum = nums[0]
        
        # Start iterating from the second element
        for i in range(1, len(nums)):
            # Either start a new subarray or extend the current one
            current_sum = max(nums[i], current_sum + nums[i])
            
            # Update the global maximum
            max_sum = max(max_sum, current_sum)
            
        return max_sum