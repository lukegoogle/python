from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """Generates all possible permutations of a list of distinct integers.

        Args:
            nums: A list of distinct integers.

        Returns:
            A list of lists, where each inner list is a unique permutation.
        """
        res = []
        # Use a 'used' array for O(1) lookups of whether an element is in path
        used = [False] * len(nums)
        
        def backtrack(path):
            # Base case: if path length matches nums length, we have a permutation
            if len(path) == len(nums):
                res.append(list(path))
                return
            
            for i in range(len(nums)):
                if not used[i]:
                    # Choose
                    used[i] = True
                    path.append(nums[i])
                    
                    # Explore
                    backtrack(path)
                    
                    # Backtrack
                    path.pop()
                    used[i] = False
                    
        backtrack([])
        return res