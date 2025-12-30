from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        """Calculates the minimum depth of a binary tree.

        Args:
            root: The root node of the binary tree.

        Returns:
            The number of nodes along the shortest path to a leaf.
        """
        # Base case: Empty tree has depth 0
        if not root:
            return 0
        
        # If no left child, we must go right
        if not root.left:
            return 1 + self.minDepth(root.right)
        
        # If no right child, we must go left
        if not root.right:
            return 1 + self.minDepth(root.left)
        
        # If both children exist, find the minimum of the two paths
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))