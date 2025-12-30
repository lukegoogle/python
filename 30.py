from typing import List
from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        """Finds starting indices of substrings that concatenate all words.

        Args:
            s: The source string to search.
            words: A list of strings, all of the same length.

        Returns:
            A list of starting indices where the concatenation is found.
        """
        if not s or not words:
            return []
            
        word_len = len(words[0])
        num_words = len(words)
        total_len = word_len * num_words
        word_count = Counter(words)
        results = []
        
        # We only need to check starting offsets from 0 to word_len - 1
        for i in range(word_len):
            left = i
            right = i
            current_count = Counter()
            words_found = 0
            
            # Slide the window in word_len increments
            while right + word_len <= len(s):
                word = s[right : right + word_len]
                right += word_len
                
                if word in word_count:
                    current_count[word] += 1
                    words_found += 1
                    
                    # If we have more of 'word' than required, shrink from left
                    while current_count[word] > word_count[word]:
                        left_word = s[left : left + word_len]
                        current_count[left_word] -= 1
                        words_found -= 1
                        left += word_len
                    
                    # If window size matches target, record the starting index
                    if words_found == num_words:
                        results.append(left)
                else:
                    # Not a valid word: reset the window
                    current_count.clear()
                    words_found = 0
                    left = right
                    
        return results