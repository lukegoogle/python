from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        """Finds all unique quadruplets that sum to the target.

        Args:
            nums: A list of integers.
            target: The desired sum.

        Returns:
            A list of unique quadruplets.
        """
        nums.sort()
        results = []
        
        def kSum(start: int, target: int, k: int, path: List[int]):
            # Base Case: Use two pointers for 2Sum
            if k == 2:
                l, r = start, len(nums) - 1
                while l < r:
                    curr_sum = nums[l] + nums[r]
                    if curr_sum == target:
                        results.append(path + [nums[l], nums[r]])
                        l += 1
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
                    elif curr_sum < target:
                        l += 1
                    else:
                        r -= 1
                return

            # Recursive Step: Reduce k-Sum to (k-1)-Sum
            for i in range(start, len(nums) - k + 1):
                # Skip duplicates
                if i > start and nums[i] == nums[i-1]:
                    continue
                
                # Optimization: Pruning
                # If the smallest k numbers are > target, or largest < target, stop
                if nums[i] * k > target or nums[-1] * k < target:
                    break
                    
                kSum(i + 1, target - nums[i], k - 1, path + [nums[i]])

        kSum(0, target, 4, [])
        return results