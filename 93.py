from typing import List

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        """Generates all possible valid IP addresses from a string of digits.

        Args:
            s: A string containing only digits.

        Returns:
            A list of strings representing all valid IP address combinations.
        """
        res = []
        
        # If the string is too short or too long, it can't be a valid IP
        if len(s) < 4 or len(s) > 12:
            return res

        def backtrack(start: int, dots: int, current_ip: List[str]):
            """Explores potential IP segments using backtracking.

            Args:
                start: The starting index in the string s.
                dots: The number of dots already placed.
                current_ip: List of segments currently in the IP address.
            """
            # Base case: if we have 4 segments and used all characters
            if dots == 4:
                if start == len(s):
                    res.append(".".join(current_ip))
                return

            # Try taking 1, 2, or 3 characters for the next segment
            for length in range(1, 4):
                if start + length > len(s):
                    break
                
                segment = s[start : start + length]
                
                # Check for leading zeros: '0' is okay, '01' is not
                if length > 1 and segment[0] == '0':
                    continue
                
                # Check if the segment value is within range 0-255
                if int(segment) <= 255:
                    current_ip.append(segment)
                    backtrack(start + length, dots + 1, current_ip)
                    # Backtrack: remove the last segment added
                    current_ip.pop()

        backtrack(0, 0, [])
        return res