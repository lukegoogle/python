class Solution:
    def countAndSay(self, n: int) -> str:
        """Generates the nth term of the count-and-say sequence.

        Args:
            n: The index of the term to generate (1-indexed).

        Returns:
            The nth term of the sequence as a string.
        """
        if n == 1:
            return "1"
        
        # Start with the first term
        current_str = "1"
        
        # Generate terms from 2 to n
        for _ in range(n - 1):
            next_str = []
            i = 0
            
            while i < len(current_str):
                count = 1
                # Move pointer while characters are the same
                while i + 1 < len(current_str) and current_str[i] == current_str[i+1]:
                    i += 1
                    count += 1
                
                # Append count followed by the digit
                next_str.append(str(count))
                next_str.append(current_str[i])
                i += 1
            
            current_str = "".join(next_str)
            
        return current_str