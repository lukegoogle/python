from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """Finds the longest common prefix among an array of strings.

        Uses the horizontal scanning method to compare and trim the 
        potential prefix against each string in the list.

        Args:
            strs: A list of strings to compare.

        Returns:
            The longest common prefix shared by all strings.
        """
        if not strs:
            return ""
        
        # Start with the first string as the initial prefix
        prefix = strs[0]
        
        for i in range(1, len(strs)):
            # While the current string doesn't start with the prefix
            while not strs[i].startswith(prefix):
                # Shorten the prefix by one character from the end
                prefix = prefix[:-1]
                
                # If prefix becomes empty, no common prefix exists
                if not prefix:
                    return ""
                    
        return prefix