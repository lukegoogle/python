from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """Generates all combinations of n pairs of well-formed parentheses.

        Uses a backtracking approach to build valid strings by maintaining
        counts of open and closed brackets.

        Args:
            n: The number of pairs of parentheses.

        Returns:
            A list of strings containing all valid combinations.
        """
        res = []
        
        def backtrack(current_string: str, open_count: int, close_count: int):
            # Base case: if the string has reached the maximum length (2 * n)
            if len(current_string) == 2 * n:
                res.append(current_string)
                return
            
            # If we can still add an opening bracket
            if open_count < n:
                backtrack(current_string + "(", open_count + 1, close_count)
            
            # If we can add a closing bracket (must be fewer than open brackets)
            if close_count < open_count:
                backtrack(current_string + ")", open_count, close_count + 1)
                
        backtrack("", 0, 0)
        return res