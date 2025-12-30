from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        """Determines if a binary tree is symmetric around its center.

        Args:
            root: The root node of the binary tree.

        Returns:
            True if the tree is symmetric, False otherwise.
        """
        if not root:
            return True
        
        return self.is_mirror(root.left, root.right)

    def is_mirror(self, t1: Optional[TreeNode], t2: Optional[TreeNode]) -> bool:
        """Helper function to check if two subtrees are mirror images.

        Args:
            t1: The root of the first subtree.
            t2: The root of the second subtree.

        Returns:
            True if t1 and t2 are mirrors of each other.
        """
        # If both are null, they are mirrors
        if not t1 and not t2:
            return True
        
        # If only one is null, or values don't match, they are not mirrors
        if not t1 or not t2 or t1.val != t2.val:
            return False
        
        # Check 'outside' children (t1.left and t2.right) 
        # and 'inside' children (t1.right and t2.left)
        return (self.is_mirror(t1.left, t2.right) and 
                self.is_mirror(t1.right, t2.left))