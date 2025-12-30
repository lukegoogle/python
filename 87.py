class Solution:
    def __init__(self):
        # Memoization dictionary to store results of (s1, s2) pairs
        self.memo = {}

    def isScramble(self, s1: str, s2: str) -> bool:
        """Determines if s2 is a scrambled string of s1.

        Args:
            s1: The original string.
            s2: The string to check against s1.

        Returns:
            True if s2 is a scrambled version of s1, False otherwise.
        """
        # Check memo first
        if (s1, s2) in self.memo:
            return self.memo[(s1, s2)]
        
        # Base cases
        if s1 == s2:
            return True
        if sorted(s1) != sorted(s2): # Pruning: must have same characters
            self.memo[(s1, s2)] = False
            return False
        
        n = len(s1)
        for i in range(1, n):
            # Case 1: No swap at this level
            # Check s1[:i] with s2[:i] and s1[i:] with s2[i:]
            if self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]):
                self.memo[(s1, s2)] = True
                return True
            
            # Case 2: Swap occurred at this level
            # Check s1[:i] with s2[n-i:] and s1[i:] with s2[:n-i]
            if self.isScramble(s1[:i], s2[n-i:]) and self.isScramble(s1[i:], s2[:n-i]):
                self.memo[(s1, s2)] = True
                return True
        
        self.memo[(s1, s2)] = False
        return False