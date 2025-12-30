from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        """Calculates the minimum number of jumps to reach the last index.

        Args:
            nums: A list of non-negative integers representing max jump lengths.

        Returns:
            The minimum number of jumps required.
        """
        # If the array has only one element, we are already at the end
        if len(nums) <= 1:
            return 0
            
        jumps = 0
        current_jump_end = 0
        farthest_reach = 0
        
        # Iterate up to the second to last element
        for i in range(len(nums) - 1):
            # Update the farthest we can reach from the current position
            farthest_reach = max(farthest_reach, i + nums[i])
            
            # If we've reached the end of the current jump's range
            if i == current_jump_end:
                jumps += 1
                current_jump_end = farthest_reach
                
                # If the new range already reaches or exceeds the end, we can stop
                if current_jump_end >= len(nums) - 1:
                    break
                    
        return jumps