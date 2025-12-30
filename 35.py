from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """Finds the index of a target or its sorted insertion position.

        Args:
            nums: A sorted list of distinct integers.
            target: The integer value to search for.

        Returns:
            The index of the target if found, or the index where it
            would be inserted to maintain order.
        """
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
                
        # If not found, 'left' is the insertion index
        return left