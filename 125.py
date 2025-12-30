class Solution:
    def isPalindrome(self, s: str) -> bool:
        """Determines if a string is a palindrome, ignoring non-alphanumeric chars.

        This implementation uses two pointers to achieve O(1) auxiliary space.

        Args:
            s: The input string to check.

        Returns:
            True if the string is a palindrome, False otherwise.
        """
        left, right = 0, len(s) - 1

        while left < right:
            # Skip non-alphanumeric characters from the left
            while left < right and not s[left].isalnum():
                left += 1
            
            # Skip non-alphanumeric characters from the right
            while left < right and not s[right].isalnum():
                right -= 1
            
            # Compare lowercase versions of the characters
            if s[left].lower() != s[right].lower():
                return False
            
            # Move pointers inward
            left += 1
            right -= 1
            
        return True