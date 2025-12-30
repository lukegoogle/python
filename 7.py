class Solution:
    def reverse(self, x: int) -> int:
        """Reverses a signed 32-bit integer.

        Args:
            x: The integer to be reversed.

        Returns:
            The reversed integer, or 0 if the reversed integer overflows 
            the signed 32-bit range [-2^31, 2^31 - 1].
        """
        # Define 32-bit signed integer limits
        MIN_INT = -2147483648
        MAX_INT = 2147483647
        
        res = 0
        # Determine sign and work with absolute value for easier modulo
        sign = -1 if x < 0 else 1
        x = abs(x)
        
        while x != 0:
            # Get the last digit
            pop = x % 10
            x //= 10
            
            # Check for overflow before updating res
            # res * 10 + pop > MAX_INT  =>  res > (MAX_INT - pop) / 10
            if res > (MAX_INT - pop) // 10:
                return 0
                
            res = res * 10 + pop
            
        return res * sign