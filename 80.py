from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """Removes duplicates from a sorted array such that elements appear at most twice.

        The removal is done in-place, and the relative order of the elements 
        is maintained.

        Args:
            nums: A list of integers sorted in non-decreasing order.

        Returns:
            The number of elements in nums after removing extra duplicates.
        """
        if len(nums) <= 2:
            return len(nums)
        
        # 'k' is the index where we will write the next valid element.
        # We start at 2 because the first two elements are always allowed.
        k = 2
        
        for i in range(2, len(nums)):
            # If the current element is not the same as the element
            # two positions before the current write index 'k'.
            if nums[i] != nums[k - 2]:
                nums[k] = nums[i]
                k += 1
                
        return k