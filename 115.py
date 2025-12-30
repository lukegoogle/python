class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        """Counts the number of distinct subsequences of s that equal t.

        Args:
            s: The source string.
            t: The target string.

        Returns:
            The number of distinct subsequences.
        """
        # Cache to store results of subproblems (memoization)
        memo = {}

        def dp(i: int, j: int) -> int:
            """Recursive helper to find distinct subsequences.

            Args:
                i: Current index in string s.
                j: Current index in string t.

            Returns:
                Number of distinct subsequences for the current suffixes.
            """
            # Base Case: If we matched all characters of t
            if j == len(t):
                return 1
            # Base Case: If s is exhausted but t isn't
            if i == len(s):
                return 0
            
            # Check if already computed
            if (i, j) in memo:
                return memo[(i, j)]

            # If characters match, we can either use s[i] or skip it
            if s[i] == t[j]:
                res = dp(i + 1, j + 1) + dp(i + 1, j)
            else:
                # If they don't match, we must skip s[i]
                res = dp(i + 1, j)
            
            memo[(i, j)] = res
            return res

        return dp(0, 0)