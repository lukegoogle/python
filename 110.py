from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """Determines if a binary tree is height-balanced.

        A tree is balanced if the heights of the two subtrees of every node 
        never differ by more than one.

        Args:
            root: The root node of the binary tree.

        Returns:
            True if the tree is balanced, False otherwise.
        """
        def get_height(node: Optional[TreeNode]) -> int:
            """Calculates height if balanced, otherwise returns -1.

            Args:
                node: The current node to check.

            Returns:
                The height of the node or -1 if the subtree is unbalanced.
            """
            if not node:
                return 0
            
            # Check left subtree
            left_height = get_height(node.left)
            if left_height == -1:
                return -1
            
            # Check right subtree
            right_height = get_height(node.right)
            if right_height == -1:
                return -1
            
            # Check current node's balance
            if abs(left_height - right_height) > 1:
                return -1
            
            # Return actual height if balanced
            return 1 + max(left_height, right_height)

        return get_height(root) != -1