from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """Generates all possible subsets from a list that may contain duplicates.

        Args:
            nums: A list of integers.

        Returns:
            A list of lists, where each inner list is a unique subset.
        """
        # Sort to ensure duplicates are adjacent
        nums.sort()
        results = []
        
        def backtrack(start: int, current_subset: List[int]):
            """Explores subset combinations using DFS.

            Args:
                start: The index to start exploring from in nums.
                current_subset: The subset built in the current recursion path.
            """
            # Add a copy of the current subset to the results
            results.append(list(current_subset))
            
            for i in range(start, len(nums)):
                # If the current element is the same as the previous one
                # AND it's not the first element in this loop level, skip it.
                if i > start and nums[i] == nums[i - 1]:
                    continue
                
                # Include nums[i] in the subset
                current_subset.append(nums[i])
                # Move to the next element
                backtrack(i + 1, current_subset)
                # Backtrack: remove nums[i] to try the next possibility
                current_subset.pop()

        backtrack(0, [])
        return results