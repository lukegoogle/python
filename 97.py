class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        """Determines if s3 is an interleaving of s1 and s2.

        Args:
            s1: The first source string.
            s2: The second source string.
            s3: The target string to check for interleaving.

        Returns:
            True if s3 is a valid interleaving, False otherwise.
        """
        n, m = len(s1), len(s2)
        
        # Base check: total length must match
        if n + m != len(s3):
            return False
            
        # dp[i][j] means s1[:i] and s2[:j] can form s3[:i+j]
        dp = [[False] * (m + 1) for _ in range(n + 1)]
        
        for i in range(n + 1):
            for j in range(m + 1):
                # Base case: empty strings interleave to form empty string
                if i == 0 and j == 0:
                    dp[i][j] = True
                # Case 1: s1 is empty, check s2 against s3
                elif i == 0:
                    dp[i][j] = dp[i][j-1] and s2[j-1] == s3[i+j-1]
                # Case 2: s2 is empty, check s1 against s3
                elif j == 0:
                    dp[i][j] = dp[i-1][j] and s1[i-1] == s3[i+j-1]
                # Case 3: Both strings have characters
                else:
                    # Check if s3's last char came from s1 OR s2
                    from_s1 = dp[i-1][j] and s1[i-1] == s3[i+j-1]
                    from_s2 = dp[i][j-1] and s2[j-1] == s3[i+j-1]
                    dp[i][j] = from_s1 or from_s2
                    
        return dp[n][m]