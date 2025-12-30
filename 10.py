class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """Determines if a string matches a pattern with '.' and '*'.

        Uses top-down dynamic programming (memoization) to explore 
        matching possibilities.

        Args:
            s: The input string.
            p: The pattern string.

        Returns:
            True if the pattern matches the entire string, False otherwise.
        """
        memo = {}

        def dp(i: int, j: int) -> bool:
            # Check if result is already computed
            if (i, j) in memo:
                return memo[(i, j)]
            
            # Base case: if we reach the end of the pattern
            if j == len(p):
                return i == len(s)

            # Check if the first characters match
            first_match = i < len(s) and (p[j] == s[i] or p[j] == '.')

            # Handle the '*' wildcard
            if j + 1 < len(p) and p[j+1] == '*':
                # Two choices:
                # 1. Skip the '*' and its preceding element (match zero times)
                # 2. Use the '*' if first_match is true (match one or more times)
                res = dp(i, j + 2) or (first_match and dp(i + 1, j))
            else:
                # Regular match (single character or '.')
                res = first_match and dp(i + 1, j + 1)

            memo[(i, j)] = res
            return res

        return dp(0, 0)