from typing import List, Dict

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        """Constructs all possible sentences from a string and a dictionary.

        Args:
            s: The input string to be segmented.
            wordDict: A list of valid words.

        Returns:
            A list of all possible space-separated sentences.
        """
        word_set = set(wordDict)
        # memo stores: {substring: [list of valid segmentations]}
        memo: Dict[str, List[str]] = {}

        def backtrack(remaining_s: str) -> List[str]:
            """Recursively finds all ways to segment the remaining string.

            Args:
                remaining_s: The suffix of the original string currently being processed.

            Returns:
                A list of valid sentences for the current suffix.
            """
            # If we've already solved this substring, return the cached result
            if remaining_s in memo:
                return memo[remaining_s]
            
            # Base case: if the remaining string is empty, return an empty string
            # to signify a valid path has been completed.
            if not remaining_s:
                return [""]

            res = []
            # Try every possible split point
            for i in range(1, len(remaining_s) + 1):
                prefix = remaining_s[:i]
                
                if prefix in word_set:
                    # Get all ways to segment the rest of the string
                    suffixes = backtrack(remaining_s[i:])
                    
                    for suffix in suffixes:
                        # Join prefix with suffixes, handling the trailing space
                        sentence = (prefix + (" " if suffix else "") + suffix)
                        res.append(sentence)
            
            memo[remaining_s] = res
            return res

        return backtrack(s)