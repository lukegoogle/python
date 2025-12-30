class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """Finds the first occurrence of needle in haystack.

        Args:
            haystack: The string to search within.
            needle: The substring to search for.

        Returns:
            The start index of the first occurrence of needle, 
            or -1 if needle is not found.
        """
        n, m = len(haystack), len(needle)
        
        # If needle is longer than haystack, it can't be found
        if m > n:
            return -1
            
        # Slide the window across haystack
        for i in range(n - m + 1):
            # Check if the substring matches the needle
            if haystack[i : i + m] == needle:
                return i
                
        return -1