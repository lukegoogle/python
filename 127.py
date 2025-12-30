from collections import deque
from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """Finds the length of the shortest transformation sequence.

        Args:
            beginWord: The starting word.
            endWord: The target word.
            wordList: List of valid intermediate words.

        Returns:
            The number of words in the shortest sequence, or 0 if no path exists.
        """
        word_set = set(wordList)
        if endWord not in word_set:
            return 0
        
        # Queue stores (current_word, current_distance)
        queue = deque([(beginWord, 1)])
        
        # Use a set to track visited words to prevent infinite loops
        visited = {beginWord}
        
        while queue:
            current_word, level = queue.popleft()
            
            # If we reached the target, return the current level
            if current_word == endWord:
                return level
            
            # Try changing every character in the word
            for i in range(len(current_word)):
                for char in "abcdefghijklmnopqrstuvwxyz":
                    next_word = current_word[:i] + char + current_word[i+1:]
                    
                    if next_word in word_set and next_word not in visited:
                        visited.add(next_word)
                        queue.append((next_word, level + 1))
                        
        return 0