from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """Removes all occurrences of a specific value in-place.

        Args:
            nums: A list of integers.
            val: The integer value to be removed from the list.

        Returns:
            The number of elements in nums which are not equal to val.
        """
        # i keeps track of the index where the next non-val element goes
        i = 0
        
        for j in range(len(nums)):
            # If the current element is not the one we want to remove
            if nums[j] != val:
                # Move it to the 'i' position and increment 'i'
                nums[i] = nums[j]
                i += 1
                
        return i