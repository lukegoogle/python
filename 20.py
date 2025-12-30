class Solution:
    def isValid(self, s: str) -> bool:
        """Determines if a string of parentheses is valid using a stack.

        Args:
            s: A string containing only '()[]{}'.

        Returns:
            True if the string is valid, False otherwise.
        """
        # Map closing brackets to their matching opening brackets
        bracket_map = {")": "(", "}": "{", "]": "["}
        stack = []

        for char in s:
            # If the character is a closing bracket
            if char in bracket_map:
                # Pop the top element if stack is not empty, else use a dummy
                top_element = stack.pop() if stack else '#'
                
                # Check if the popped opening bracket matches the current closing one
                if bracket_map[char] != top_element:
                    return False
            else:
                # It's an opening bracket, push it onto the stack
                stack.append(char)

        # If the stack is empty, all brackets were matched correctly
        return not stack