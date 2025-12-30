from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """Searches for a target in a rotated sorted array in O(log n).

        Args:
            nums: A list of integers rotated at some pivot.
            target: The integer value to search for.

        Returns:
            The index of the target if found, otherwise -1.
        """
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
            
            # Check if the left half [left...mid] is sorted
            if nums[left] <= nums[mid]:
                # If target is within the sorted left half
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # Otherwise, the right half [mid...right] must be sorted
            else:
                # If target is within the sorted right half
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
                    
        return -1