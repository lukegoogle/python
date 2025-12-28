class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # Edge case: if rows = 1 or string is short, no zigzag is possible
        if numRows == 1 or numRows >= len(s):
            return s
        
        # Create a list for each row
        rows = [[] for _ in range(numRows)]
        index = 0
        step = 1 # 1 means moving down, -1 means moving up
        
        for char in s:
            rows[index].append(char)
            
            # If at the top row, move down
            if index == 0:
                step = 1
            # If at the bottom row, move up
            elif index == numRows - 1:
                step = -1
                
            index += step
            
        # Join all characters in each row, then join the rows
        return "".join(["".join(row) for row in rows])