from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """Finds all unique combinations that sum up to target using each number once.

        Args:
            candidates: A list of integers (may contain duplicates).
            target: The target sum to achieve.

        Returns:
            A list of all unique combinations that sum to target.
        """
        res = []
        # Sorting is essential for duplicate handling and early pruning
        candidates.sort()
        
        def backtrack(remain: int, combo: List[int], start: int):
            if remain == 0:
                res.append(list(combo))
                return
            
            for i in range(start, len(candidates)):
                # Skip duplicates at the same recursive level
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                
                # Optimization: stop if the number exceeds the remaining target
                if candidates[i] > remain:
                    break
                
                combo.append(candidates[i])
                # i + 1 ensures each candidate is used only once
                backtrack(remain - candidates[i], combo, i + 1)
                combo.pop()
        
        backtrack(target, [], 0)
        return res