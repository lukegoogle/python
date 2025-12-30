class Solution:
    def minCut(self, s: str) -> int:
        """Calculates the minimum cuts needed for palindromic partitioning.

        Args:
            s: The input string.

        Returns:
            The minimum number of cuts required.
        """
        n = len(s)
        # is_pal[i][j] will be True if s[i:j+1] is a palindrome
        is_pal = [[False] * n for _ in range(n)]
        
        # dp[i] is the min cuts for s[0:i]
        # Initialize with maximum possible cuts: each char is a partition
        dp = [i for i in range(n)]

        for i in range(n):
            for j in range(i + 1):
                # Check if s[j:i+1] is a palindrome
                # 1. Characters at boundaries must match
                # 2. Inner substring must be a palindrome or length <= 2
                if s[i] == s[j] and (i - j <= 2 or is_pal[j + 1][i - 1]):
                    is_pal[j][i] = True
                    
                    if j == 0:
                        # The whole prefix s[0:i+1] is a palindrome
                        dp[i] = 0
                    else:
                        # Cut after s[j-1] and the remaining s[j:i+1] is a palindrome
                        dp[i] = min(dp[i], dp[j - 1] + 1)
                        
        return dp[n - 1]