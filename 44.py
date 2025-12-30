class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """Determines if a string matches a wildcard pattern.

        Args:
            s: The input string.
            p: The pattern string containing '?' and '*'.

        Returns:
            True if the pattern matches the string, False otherwise.
        """
        sn, pn = len(s), len(p)
        
        # Initialize DP table with False
        dp = [[False] * (pn + 1) for _ in range(sn + 1)]
        
        # Base case: empty string and empty pattern
        dp[0][0] = True
        
        # Handle patterns starting with '*' for empty string s
        for j in range(1, pn + 1):
            if p[j-1] == '*':
                dp[0][j] = dp[0][j-1]
            else:
                # Once we hit a non-*, no more matches are possible for empty s
                break
                
        for i in range(1, sn + 1):
            for j in range(1, pn + 1):
                if p[j-1] == s[i-1] or p[j-1] == '?':
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*':
                    # Two cases: * acts as empty (dp[i][j-1]) 
                    # OR * matches current char and remains available (dp[i-1][j])
                    dp[i][j] = dp[i][j-1] or dp[i-1][j]
                    
        return dp[sn][pn]