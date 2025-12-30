from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        """Calculates the maximum water a container can store.

        Uses the two-pointer approach to find the maximum area in linear time.

        Args:
            height: A list of integers representing the heights of lines.

        Returns:
            The maximum volume of water that can be contained.
        """
        left = 0
        right = len(height) - 1
        max_water = 0
        
        while left < right:
            # Calculate width and the limiting height
            width = right - left
            current_height = min(height[left], height[right])
            
            # Update the maximum area found so far
            current_water = width * current_height
            max_water = max(max_water, current_water)
            
            # Move the pointer pointing to the shorter line
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return max_water