class Solution:
    def myAtoi(self, s: str) -> int:
        """Converts a string to a 32-bit signed integer (atoi).

        Args:
            s: The string to be converted.

        Returns:
            The converted integer clamped to the 32-bit signed integer 
            range [-2^31, 2^31 - 1].
        """
        s = s.lstrip()
        if not s:
            return 0
        
        sign = 1
        i = 0
        
        # Handle sign
        if s[i] == '-':
            sign = -1
            i += 1
        elif s[i] == '+':
            i += 1
            
        res = 0
        MAX_INT = 2**31 - 1
        MIN_INT = -2**31
        
        # Convert digits
        while i < len(s) and s[i].isdigit():
            digit = int(s[i])
            
            # Check for overflow before multiplication/addition
            if res > (MAX_INT - digit) // 10:
                return MAX_INT if sign == 1 else MIN_INT
            
            res = res * 10 + digit
            i += 1
            
        return res * sign