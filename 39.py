from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """Finds all unique combinations that sum up to the target.

        Uses a backtracking approach to explore combinations, allowing for 
        unlimited reuse of candidates.

        Args:
            candidates: A list of distinct integers.
            target: The target sum to achieve.

        Returns:
            A list of all unique combinations (lists) that sum to target.
        """
        res = []
        
        def backtrack(remain: int, combo: List[int], start: int):
            # Base case: target reached
            if remain == 0:
                res.append(list(combo))
                return
            # Base case: exceeded target
            if remain < 0:
                return
            
            for i in range(start, len(candidates)):
                # Add the candidate to the current combination
                combo.append(candidates[i])
                
                # Recurse: 'i' stays the same because we can reuse the element
                backtrack(remain - candidates[i], combo, i)
                
                # Backtrack: remove the last element to try the next candidate
                combo.pop()
                
        backtrack(target, [], 0)
        return res