from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """Finds the length of the longest consecutive elements sequence.

        This implementation uses a hash set to achieve O(n) time complexity.

        Args:
            nums: An unsorted list of integers.

        Returns:
            The length of the longest consecutive sequence.
        """
        if not nums:
            return 0

        # Convert list to set for O(1) lookups
        num_set = set(nums)
        longest_streak = 0

        for num in num_set:
            # Check if 'num' is the start of a sequence.
            # If 'num - 1' is in the set, then 'num' is part of a 
            # sequence that started earlier.
            if (num - 1) not in num_set:
                current_num = num
                current_streak = 1

                # Count how long this sequence goes
                while (current_num + 1) in num_set:
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak