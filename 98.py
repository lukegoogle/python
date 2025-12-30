from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """Determines if a binary tree is a valid Binary Search Tree.

        Args:
            root: The root node of the binary tree.

        Returns:
            True if the tree is a valid BST, False otherwise.
        """
        def validate(node: Optional[TreeNode], low: float, high: float) -> bool:
            """Helper function to validate node values within a specific range.

            Args:
                node: The current node being validated.
                low: The lower bound for the node's value.
                high: The upper bound for the node's value.

            Returns:
                True if the subtree rooted at node is a valid BST.
            """
            # An empty tree is a valid BST
            if not node:
                return True
            
            # The current node's value must be strictly within (low, high)
            if not (low < node.val < high):
                return False
            
            # Recursively validate subtrees with updated ranges
            # Left child must be < node.val
            # Right child must be > node.val
            return (validate(node.left, low, node.val) and 
                    validate(node.right, node.val, high))

        # Initialize with infinity to allow any value at the root
        return validate(root, float('-inf'), float('inf'))