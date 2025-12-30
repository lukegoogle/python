from collections import deque, defaultdict
from typing import List

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[int]]:
        """Finds all shortest transformation sequences from beginWord to endWord.

        Args:
            beginWord: The starting word.
            endWord: The target word.
            wordList: The list of available words for transformation.

        Returns:
            A list of all shortest transformation sequences.
        """
        word_set = set(wordList)
        if endWord not in word_set:
            return []

        # Step 1: BFS to find the shortest distance to each word
        # and build an adjacency list of the shortest paths.
        adj = defaultdict(list)
        distances = {beginWord: 0}
        queue = deque([beginWord])
        found = False
        
        while queue and not found:
            current_level_visited = set()
            for _ in range(len(queue)):
                word = queue.popleft()
                
                # Generate all possible one-letter transformations
                for i in range(len(word)):
                    for char in 'abcdefghijklmnopqrstuvwxyz':
                        next_word = word[:i] + char + word[i+1:]
                        
                        if next_word in word_set:
                            # If this is the first time we see this word, 
                            # or it's at the next level
                            if next_word not in distances or distances[next_word] == distances[word] + 1:
                                if next_word not in distances:
                                    distances[next_word] = distances[word] + 1
                                    queue.append(next_word)
                                    current_level_visited.add(next_word)
                                
                                # Add to our shortest-path graph
                                adj[word].append(next_word)
                                if next_word == endWord:
                                    found = True
                                    
        # Step 2: DFS (Backtracking) to reconstruct all paths
        results = []
        def backtrack(current_word: str, path: List[str]):
            """Reconstructs paths using the adjacency list from BFS.

            Args:
                current_word: The current word in the backtracking.
                path: The current path being built.
            """
            if current_word == endWord:
                results.append(list(path))
                return
            
            for next_word in adj[current_word]:
                # Only follow the path if it leads to a shorter distance
                if distances.get(next_word) == distances[current_word] + 1:
                    path.append(next_word)
                    backtrack(next_word, path)
                    path.pop()

        backtrack(beginWord, [beginWord])
        return results