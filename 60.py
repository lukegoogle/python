import math

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        """Finds the k-th permutation sequence of numbers 1 to n.

        Args:
            n: The number of elements in the set.
            k: The index of the permutation to find.

        Returns:
            The k-th permutation sequence as a string.
        """
        # Create a list of numbers to pick from
        numbers = [str(i) for i in range(1, n + 1)]
        
        # Precompute factorials up to (n-1)
        factorials = [1] * n
        for i in range(1, n):
            factorials[i] = factorials[i-1] * i
            
        # Adjust k to be 0-indexed
        k -= 1
        
        res = []
        # Build the permutation digit by digit
        for i in range(n - 1, -1, -1):
            # Calculate which index in the 'numbers' list we need
            # index = k // (n-1)! for the first iteration
            idx = k // factorials[i]
            
            # Append the chosen digit to result and remove from pool
            res.append(numbers.pop(idx))
            
            # Update k for the next position
            k %= factorials[i]
            
        return "".join(res)