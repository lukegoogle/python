from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """Groups anagrams together using a hash map.

        Args:
            strs: A list of strings.

        Returns:
            A list of lists, where each inner list contains grouped anagrams.
        """
        # defaultdict(list) handles the case where a key doesn't exist yet
        anagram_map = defaultdict(list)
        
        for s in strs:
            # Step 1: Create a unique key by sorting the string
            # 'eat' -> ['a', 'e', 't'] -> 'aet'
            sorted_s = "".join(sorted(s))
            
            # Step 2: Add the original string to the corresponding group
            anagram_map[sorted_s].append(s)
            
        # Return all the values (the groups) as a list
        return list(anagram_map.values())