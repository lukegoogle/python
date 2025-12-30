from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """Modifies nums in-place to the next lexicographical permutation.

        Args:
            nums: A list of integers to be permuted.
        """
        n = len(nums)
        pivot = -1
        
        # Step 1: Find the first decreasing element from the right
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                pivot = i
                break
        
        # If no pivot is found, the array is in descending order
        if pivot == -1:
            nums.reverse()
            return
            
        # Step 2: Find the element to swap with the pivot
        for j in range(n - 1, pivot, -1):
            if nums[j] > nums[pivot]:
                nums[pivot], nums[j] = nums[j], nums[pivot]
                break
        
        # Step 3: Reverse the elements to the right of the pivot
        left, right = pivot + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1