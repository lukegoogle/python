from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """Finds all unique triplets in an array that sum to zero.

        Args:
            nums: A list of integers.

        Returns:
            A list of lists, where each sublist is a unique triplet 
            that sums to zero.
        """
        res = []
        nums.sort()
        
        for i in range(len(nums)):
            # If the current number is > 0, no triplet starting here can sum to 0
            if nums[i] > 0:
                break
                
            # Skip duplicate values for the first element
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            # Use two pointers for the remaining two elements
            l, r = i + 1, len(nums) - 1
            while l < r:
                three_sum = nums[i] + nums[l] + nums[r]
                
                if three_sum > 0:
                    r -= 1
                elif three_sum < 0:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    # Skip duplicate values for the second element
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                        
        return res