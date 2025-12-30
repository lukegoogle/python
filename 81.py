from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        """Searches for a target value in a rotated sorted array with duplicates.

        Args:
            nums: A list of integers representing a rotated sorted array.
            target: The integer value to search for.

        Returns:
            True if the target is found in nums, False otherwise.
        """
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return True
            
            # The "Duplicate" Edge Case: 
            # If boundaries and mid are equal, we can't tell which side is sorted.
            if nums[left] == nums[mid] == nums[right]:
                left += 1
                right -= 1
                continue
            
            # Determine which half is sorted
            if nums[left] <= nums[mid]:
                # Left half is sorted
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                # Right half is sorted
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
                    
        return False