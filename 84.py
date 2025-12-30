from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """Calculates the area of the largest rectangle in a histogram.

        Args:
            heights: A list of integers representing heights of histogram bars.

        Returns:
            The area of the largest rectangle.
        """
        # Add a sentinel 0 to the end to force the stack to empty at the finish
        heights.append(0)
        stack = [-1]  # Stack stores indices; -1 acts as a left boundary
        max_area = 0
        
        for i in range(len(heights)):
            # While the current bar is shorter than the bar at the stack's top
            while heights[i] < heights[stack[-1]]:
                # Height of the rectangle is the bar we are popping
                h = heights[stack.pop()]
                # Width is the distance between current index and new stack top
                w = i - stack[-1] - 1
                max_area = max(max_area, h * w)
            
            stack.append(i)
            
        # Restore the original list if necessary (good practice)
        heights.pop()
        return max_area