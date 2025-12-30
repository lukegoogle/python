class Solution:
    def isNumber(self, s: str) -> bool:
        """Determines if a string is a valid number using a DFA.

        Args:
            s: The string to be evaluated.

        Returns:
            True if the string represents a valid number, False otherwise.
        """
        # Define the DFA state transitions
        # States: 
        # 0: Start, 1: Sign, 2: Digit, 3: Dot (no leading digit), 
        # 4: Digit (after dot), 5: Exponent, 6: Sign (after exponent), 
        # 7: Digit (after exponent)
        state = 0
        
        # Group characters into transition types
        def get_type(char):
            if char.isdigit(): return "digit"
            if char in "+-": return "sign"
            if char in "eE": return "exp"
            if char == ".": return "dot"
            return "invalid"

        # Transition table: {current_state: {char_type: next_state}}
        transitions = [
            {"sign": 1, "digit": 2, "dot": 3},  # State 0: Start
            {"digit": 2, "dot": 3},             # State 1: Sign
            {"digit": 2, "dot": 4, "exp": 5},  # State 2: Digit (before dot)
            {"digit": 4},                       # State 3: Dot (no leading digit)
            {"digit": 4, "exp": 5},             # State 4: Digit (after dot)
            {"sign": 6, "digit": 7},            # State 5: Exponent
            {"digit": 7},                       # State 6: Sign (after exponent)
            {"digit": 7}                        # State 7: Digit (after exponent)
        ]
        
        for char in s:
            char_type = get_type(char)
            if char_type not in transitions[state]:
                return False
            state = transitions[state][char_type]
            
        # Accepting states: where a number is considered complete
        return state in [2, 4, 7]