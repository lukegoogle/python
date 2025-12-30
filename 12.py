class Solution:
    def intToRoman(self, num: int) -> str:
        """Converts an integer to a Roman numeral string.

        Args:
            num: An integer between 1 and 3999.

        Returns:
            The Roman numeral representation of the integer.
        """
        # Define the mapping of values to Roman symbols in descending order
        value_map = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
        ]
        
        roman_parts = []
        
        for value, symbol in value_map:
            if num == 0:
                break
            
            # Determine how many times the current symbol fits into num
            count, num = divmod(num, value)
            # Append the symbol 'count' times
            roman_parts.append(symbol * count)
            
        return "".join(roman_parts)