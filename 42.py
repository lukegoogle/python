from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        """Calculates the total amount of rainwater trapped.

        Uses the two-pointer technique to find the water trapped above 
        each bar in O(n) time and O(1) space.

        Args:
            height: A list of integers representing elevation.

        Returns:
            Total units of water trapped.
        """
        if not height:
            return 0
            
        left, right = 0, len(height) - 1
        left_max, right_max = 0, 0
        water = 0
        
        while left < right:
            # The water level is bottlenecked by the lower side
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    water += left_max - height[left]
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    water += right_max - height[right]
                right -= 1
                
        return water