from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """Merges nums2 into nums1 as one sorted array in-place.

        Args:
            nums1: The first sorted array with size m + n.
            m: The number of initial elements in nums1.
            nums2: The second sorted array with size n.
            n: The number of elements in nums2.
        """
        # Pointer for the end of the actual data in nums1
        p1 = m - 1
        # Pointer for the end of nums2
        p2 = n - 1
        # Pointer for the very end of the nums1 buffer
        p = m + n - 1
        
        # Compare elements from the back and move the larger one to the end
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1
        
        # If there are remaining elements in nums2, copy them.
        # Note: If there are remaining elements in nums1, they are 
        # already in the correct place.
        if p2 >= 0:
            nums1[:p2 + 1] = nums2[:p2 + 1]