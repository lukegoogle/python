from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        """Finds the sum of three integers closest to the target.

        Args:
            nums: A list of integers.
            target: The target sum to approach.

        Returns:
            The sum of the triplet that is closest to the target.
        """
        nums.sort()
        closest_sum = float('inf')
        n = len(nums)
        
        for i in range(n - 2):
            # Optimization: skip duplicates for the first pointer
            if i > 0 and nums[i] == nums[i-1]:
                continue
                
            l, r = i + 1, n - 1
            
            while l < r:
                current_sum = nums[i] + nums[l] + nums[r]
                
                # If we hit the target exactly, we can't get any closer
                if current_sum == target:
                    return current_sum
                
                # Update the closest sum if the current one is nearer to target
                if abs(target - current_sum) < abs(target - closest_sum):
                    closest_sum = current_sum
                
                # Move pointers based on how the sum compares to the target
                if current_sum < target:
                    l += 1
                else:
                    r -= 1
                    
        return int(closest_sum)