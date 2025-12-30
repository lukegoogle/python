from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        """Determines if a root-to-leaf path exists with the given target sum.

        Args:
            root: The root node of the binary tree.
            targetSum: The target integer sum to find.

        Returns:
            True if such a path exists, False otherwise.
        """
        # Base case: An empty tree has no paths
        if not root:
            return False
        
        # Check if the current node is a leaf
        if not root.left and not root.right:
            return root.val == targetSum
        
        # Recursive step: Subtract current value and check subtrees
        remaining_sum = targetSum - root.val
        return (self.hasPathSum(root.left, remaining_sum) or 
                self.hasPathSum(root.right, remaining_sum))