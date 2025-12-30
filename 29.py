class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        """Divides two integers without using multiplication or division.

        Args:
            dividend: The number to be divided.
            divisor: The number to divide by.

        Returns:
            The integer quotient, clamped to the 32-bit signed range.
        """
        # Constants for 32-bit integer limits
        MAX_INT = 2147483647
        MIN_INT = -2147483648
        
        # Edge case: overflow
        if dividend == MIN_INT and divisor == -1:
            return MAX_INT
        
        # Determine the sign of the result
        is_negative = (dividend < 0) != (divisor < 0)
        
        # Use absolute values
        a, b = abs(dividend), abs(divisor)
        quotient = 0
        
        # Exponential search / Bit shifting approach
        while a >= b:
            temp_divisor = b
            multiple = 1
            # Double the divisor until it's larger than the remaining dividend
            while a >= (temp_divisor << 1):
                temp_divisor <<= 1
                multiple <<= 1
            
            # Subtract the largest found multiple and add to quotient
            a -= temp_divisor
            quotient += multiple
            
        return -quotient if is_negative else quotient