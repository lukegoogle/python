from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        """Converts a sorted array into a height-balanced BST.

        Args:
            nums: A list of integers sorted in ascending order.

        Returns:
            The root of the height-balanced BST.
        """
        def build_bst(left: int, right: int) -> Optional[TreeNode]:
            """Recursive helper to build BST using array indices.

            Args:
                left: The starting index of the current sub-array.
                right: The ending index of the current sub-array.

            Returns:
                The root node of the subtree.
            """
            if left > right:
                return None
            
            # Choose the middle element to ensure height balance
            # (left + right) // 2 always picks the left-middle for even sizes
            mid = (left + right) // 2
            
            root = TreeNode(nums[mid])
            
            # Recursively build left and right subtrees
            root.left = build_bst(left, mid - 1)
            root.right = build_bst(mid + 1, right)
            
            return root
            
        return build_bst(0, len(nums) - 1)