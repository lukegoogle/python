from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """Finds the starting and ending position of a target value.

        Uses two separate binary searches to find the left and right 
        boundaries of the target.

        Args:
            nums: A sorted list of integers.
            target: The integer value to search for.

        Returns:
            A list of two integers [start, end].
        """
        def find_bound(is_left: bool) -> int:
            left, right = 0, len(nums) - 1
            bound = -1
            
            while left <= right:
                mid = (left + right) // 2
                
                if nums[mid] == target:
                    bound = mid
                    if is_left:
                        # Continue searching to the left
                        right = mid - 1
                    else:
                        # Continue searching to the right
                        left = mid + 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return bound

        return [find_bound(True), find_bound(False)]