class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        """Calculates the length of the last word in a string.

        Args:
            s: A string consisting of words and spaces.

        Returns:
            The length of the last word.
        """
        length = 0
        i = len(s) - 1
        
        # Step 1: Skip trailing spaces
        while i >= 0 and s[i] == ' ':
            i -= 1
            
        # Step 2: Count characters of the last word
        while i >= 0 and s[i] != ' ':
            length += 1
            i -= 1
            
        return length