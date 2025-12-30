from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """Generates all possible letter combinations for a phone number.

        Uses a backtracking approach to traverse the digit-to-letter mappings.

        Args:
            digits: A string of digits from 2-9.

        Returns:
            A list of all possible letter combinations.
        """
        if not digits:
            return []
            
        phone_map = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        
        res = []
        
        def backtrack(index: int, path: List[str]):
            # Base case: current combination is complete
            if len(path) == len(digits):
                res.append("".join(path))
                return
            
            # Get letters for the current digit
            possible_letters = phone_map[digits[index]]
            
            for letter in possible_letters:
                # Add the letter to the current path
                path.append(letter)
                # Move to the next digit
                backtrack(index + 1, path)
                # Backtrack: remove the letter before trying the next one
                path.pop()
                
        backtrack(0, [])
        return res