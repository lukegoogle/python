class Solution:
    def climbStairs(self, n: int) -> int:
        """Calculates the number of distinct ways to climb n stairs.

        Args:
            n: The total number of steps to reach the top.

        Returns:
            The number of unique ways to reach the top.
        """
        if n <= 2:
            return n
        
        # We only need the last two values to calculate the current one
        # This is the space-optimized DP approach (O(1) space)
        first = 1  # ways to reach step 1
        second = 2 # ways to reach step 2
        
        for i in range(3, n + 1):
            current = first + second
            first = second
            second = current
            
        return second