from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """Removes duplicates from a sorted array in-place.

        Args:
            nums: A list of integers sorted in non-decreasing order.

        Returns:
            The number of unique elements in nums. The first k elements 
            of nums will contain the unique elements in their original order.
        """
        if not nums:
            return 0
        
        # i is the index of the last known unique element
        i = 0
        
        # j is the explorer pointer
        for j in range(1, len(nums)):
            # If we find a new unique element
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        
        # The number of unique elements is i + 1 (since i is 0-indexed)
        return i + 1