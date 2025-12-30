from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """Determines if a string can be segmented into dictionary words.

        Args:
            s: The input string to segment.
            wordDict: A list of available words.

        Returns:
            True if the string can be segmented, False otherwise.
        """
        # Convert to set for O(1) lookups
        word_set = set(wordDict)
        
        # dp[i] means s[0:i] can be segmented into dictionary words
        # We need n + 1 to account for the empty string base case
        n = len(s)
        dp = [False] * (n + 1)
        
        # Base case: empty string is always valid
        dp[0] = True
        
        for i in range(1, n + 1):
            for j in range(i):
                # If the prefix s[0:j] is valid AND s[j:i] is in the dictionary
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    # Optimization: once we find one valid split, move to next i
                    break
                    
        return dp[n]