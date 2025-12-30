from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """Calculates the maximum depth of a binary tree.

        Args:
            root: The root node of the binary tree.

        Returns:
            The maximum depth as an integer.
        """
        # Base case: an empty tree has depth 0
        if not root:
            return 0
        
        # Recursive case: 1 (current node) + max depth of subtrees
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        
        return 1 + max(left_depth, right_depth)