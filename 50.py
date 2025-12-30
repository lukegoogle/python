class Solution:
    def myPow(self, x: float, n: int) -> float:
        """Calculates x raised to the power n using binary exponentiation.

        Args:
            x: The base value (float).
            n: The exponent value (integer).

        Returns:
            The result of x^n.
        """
        # Handle the negative exponent case
        if n < 0:
            x = 1 / x
            n = -n
            
        res = 1
        current_product = x
        
        # Iterative Binary Exponentiation
        while n > 0:
            # If n is odd, multiply the result by the current product
            if n % 2 == 1:
                res *= current_product
            
            # Square the base and halve the exponent
            current_product *= current_product
            n //= 2
            
        return res