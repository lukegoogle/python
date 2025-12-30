class Solution:
    def mySqrt(self, x: int) -> int:
        """Computes the integer square root of a non-negative integer.

        Args:
            x: A non-negative integer.

        Returns:
            The square root of x truncated to the nearest integer.
        """
        if x < 2:
            return x
            
        left, right = 2, x // 2
        ans = 1 # For x >= 1, the root is at least 1
        
        while left <= right:
            mid = left + (right - left) // 2
            num = mid * mid
            
            if num == x:
                return mid
            elif num < x:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
                
        return ans