class Solution:
    def longestValidParentheses(self, s: str) -> int:
        """Finds the length of the longest well-formed parentheses substring.

        Uses a stack to store indices of brackets to calculate lengths
        of valid segments.

        Args:
            s: A string containing characters '(' and ')'.

        Returns:
            The length of the longest valid parentheses substring.
        """
        max_len = 0
        # Start with -1 to handle the base case for length calculation
        stack = [-1]
        
        for i, char in enumerate(s):
            if char == '(':
                # Store the index of the opening bracket
                stack.append(i)
            else:
                # Pop the matching opening bracket or the base index
                stack.pop()
                
                if not stack:
                    # Current ')' is a breaker; set new base for future lengths
                    stack.append(i)
                else:
                    # Length is current index minus index of the new stack top
                    max_len = max(max_len, i - stack[-1])
                    
        return max_len