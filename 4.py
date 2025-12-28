class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2
        
        # Ensure A is the smaller array to optimize binary search
        if len(B) < len(A):
            A, B = B, A
            
        l, r = 0, len(A) - 1
        while True:
            i = (l + r) // 2      # Partition index for A
            j = half - i - 2      # Partition index for B
            
            # Boundary values (handling out-of-bounds with infinity)
            Aleft = A[i] if i >= 0 else float("-infinity")
            Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")
            
            # Check if partition is correct
            if Aleft <= Bright and Bleft <= Aright:
                # Odd total: return the minimum of the right side
                if total % 2:
                    return min(Aright, Bright)
                # Even total: return average of max(left) and min(right)
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1