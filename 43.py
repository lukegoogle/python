class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        """Multiplies two numbers represented as strings.

        Args:
            num1: The first number as a string.
            num2: The second number as a string.

        Returns:
            The product of num1 and num2 as a string.
        """
        if num1 == "0" or num2 == "0":
            return "0"
            
        n1, n2 = len(num1), len(num2)
        # The result can have at most n1 + n2 digits
        res = [0] * (n1 + n2)
        
        # Multiply each digit from num1 and num2
        for i in range(n1 - 1, -1, -1):
            for j in range(n2 - 1, -1, -1):
                # Calculate product of current digits
                mul = int(num1[i]) * int(num2[j])
                
                # Positions in the res array
                p1, p2 = i + j, i + j + 1
                
                # Add product to the existing value at p2 (ones place)
                total = mul + res[p2]
                
                # Update positions with carry logic
                res[p2] = total % 10
                res[p1] += total // 10
                
        # Convert digit list to string, stripping leading zeros
        start = 0
        while start < len(res) and res[start] == 0:
            start += 1
            
        return "".join(map(str, res[start:]))