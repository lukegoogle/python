from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        """Finds the smallest missing positive integer in O(n) time.

        Uses the array itself as a hash map by placing each number x
        at index x - 1.

        Args:
            nums: A list of integers.

        Returns:
            The smallest positive integer not present in the list.
        """
        n = len(nums)
        
        for i in range(n):
            # While the current number is in range [1, n] and 
            # not at its correct index (i.e., nums[i] should be at nums[nums[i]-1])
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                # Swap nums[i] with the element at its target position
                # Using specific indexing to avoid pointer issues in Python
                target_idx = nums[i] - 1
                nums[i], nums[target_idx] = nums[target_idx], nums[i]
        
        # Second pass: find the first index where the value is incorrect
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        
        # If all numbers from 1 to n are present
        return n + 1