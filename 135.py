from typing import List

class Solution:
    def candy(self, ratings: List[int]) -> int:
        """Calculates the minimum candies required to satisfy neighbor requirements.

        Args:
            ratings: A list of integers representing the ratings of children.

        Returns:
            The minimum total number of candies needed.
        """
        n = len(ratings)
        # Every child starts with at least 1 candy
        candies = [1] * n

        # Left-to-Right: satisfy the left neighbor condition
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1

        # Right-to-Left: satisfy the right neighbor condition
        # We use max() to ensure we don't break the first condition
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)

        return sum(candies)