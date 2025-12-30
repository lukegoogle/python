class Solution:
    def addBinary(self, a: str, b: str) -> str:
        """Adds two binary strings and returns their sum.

        Args:
            a: The first binary string.
            b: The second binary string.

        Returns:
            The sum of the two binary strings as a new binary string.
        """
        res = []
        carry = 0
        i, j = len(a) - 1, len(b) - 1
        
        # Loop as long as there are digits to process or a carry remains
        while i >= 0 or j >= 0 or carry:
            # Get current digits or 0 if pointer is out of bounds
            val_a = int(a[i]) if i >= 0 else 0
            val_b = int(b[j]) if j >= 0 else 0
            
            # Calculate sum and new carry
            total = val_a + val_b + carry
            res.append(str(total % 2))
            carry = total // 2
            
            # Move pointers left
            i -= 1
            j -= 1
            
        return "".join(res[::-1])