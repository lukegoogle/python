from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        """Generates all unique permutations of a list that may contain duplicates.

        Args:
            nums: A list of integers, potentially including duplicates.

        Returns:
            A list of unique permutations.
        """
        res = []
        path = []
        # Sort to handle duplicates easily
        nums.sort()
        used = [False] * len(nums)
        
        def backtrack():
            # Base case: completed a permutation
            if len(path) == len(nums):
                res.append(list(path))
                return
            
            for i in range(len(nums)):
                # If already used this specific index, skip
                if used[i]:
                    continue
                
                # If this number is a duplicate of the previous number...
                # and the previous number wasn't used in this current path...
                # skip it to avoid generating the same permutation again.
                if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                    continue
                
                used[i] = True
                path.append(nums[i])
                
                backtrack()
                
                # Backtrack
                path.pop()
                used[i] = False
                
        backtrack()
        return res