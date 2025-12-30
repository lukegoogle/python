from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """Determines if two binary trees are structurally and valued identical.

        Args:
            p: The root of the first binary tree.
            q: The root of the second binary tree.

        Returns:
            True if the trees are the same, False otherwise.
        """
        # If both nodes are None, the trees are identical at this position
        if not p and not q:
            return True
        
        # If one node is None and the other is not, or if values differ
        if not p or not q or p.val != q.val:
            return False
        
        # Recursively check the left and right subtrees
        return (self.isSameTree(p.left, q.left) and 
                self.isSameTree(p.right, q.right))