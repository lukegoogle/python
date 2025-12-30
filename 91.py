class Solution:
    def numDecodings(self, s: str) -> int:
        """Calculates the total number of ways to decode a numeric string.

        Args:
            s: A string containing only digits.

        Returns:
            The number of possible ways to decode the string.
        """
        if not s or s[0] == '0':
            return 0

        n = len(s)
        # dp[i] stores the number of ways to decode s[:i]
        dp = [0] * (n + 1)
        
        # Base cases
        dp[0] = 1  # Empty string has one way to be "decoded"
        dp[1] = 1  # First char (already checked for '0') has one way
        
        for i in range(2, n + 1):
            # Check for single-digit decoding (1-9)
            one_digit = int(s[i-1:i])
            if 1 <= one_digit <= 9:
                dp[i] += dp[i-1]
                
            # Check for two-digit decoding (10-26)
            two_digits = int(s[i-2:i])
            if 10 <= two_digits <= 26:
                dp[i] += dp[i-2]
                
        return dp[n]