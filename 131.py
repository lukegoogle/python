from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        """Partitions a string into all possible palindromic substrings.

        Args:
            s: The input string to be partitioned.

        Returns:
            A list of lists, where each inner list represents a valid 
            partition of the string into palindromes.
        """
        results = []
        
        def is_palindrome(sub: str) -> bool:
            """Checks if a given string is a palindrome."""
            return sub == sub[::-1]

        def backtrack(start: int, current_path: List[str]):
            """Explores all possible partitions starting from a given index.

            Args:
                start: The starting index of the substring we are considering.
                current_path: The current list of palindromic substrings found.
            """
            # Base case: if we've reached the end of the string, add path to results
            if start == len(s):
                results.append(list(current_path))
                return

            for end in range(start + 1, len(s) + 1):
                substring = s[start:end]
                if is_palindrome(substring):
                    # Action: choose the current substring
                    current_path.append(substring)
                    # Explore: move to the next part of the string
                    backtrack(end, current_path)
                    # Backtrack: remove the choice to try other possibilities
                    current_path.pop()

        backtrack(0, [])
        return results