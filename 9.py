class Solution:
    def isPalindrome(self, x: int) -> bool:
        """Determines if an integer is a palindrome without string conversion.

        Args:
            x: The integer to check.

        Returns:
            True if x is a palindrome, False otherwise.
        """
        # Special cases:
        # Negative numbers are not palindromes.
        # Numbers ending in 0 (except 0 itself) are not palindromes.
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reverted_number = 0
        # Reverse only the second half of the number
        while x > reverted_number:
            reverted_number = reverted_number * 10 + x % 10
            x //= 10

        # For even digits (1221), x will be 12 and reverted_number will be 12.
        # For odd digits (121), x will be 1 and reverted_number will be 12.
        # We get rid of the middle digit by reverted_number // 10.
        return x == reverted_number or x == reverted_number // 10