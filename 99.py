from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """Finds and swaps two incorrectly placed nodes in a BST.

        Do not return anything, modify root in-place instead.

        Args:
            root: The root of the binary search tree.
        """
        # first and second will store the two nodes to be swapped
        # prev will track the previously visited node in inorder traversal
        self.first = None
        self.second = None
        self.prev = TreeNode(float('-inf'))

        def inorder(node: Optional[TreeNode]):
            """Recursive helper for inorder traversal.

            Args:
                node: The current node in the traversal.
            """
            if not node:
                return
            
            inorder(node.left)

            # Detect the swapped nodes
            if node.val < self.prev.val:
                # If first is None, this is the first violation found
                if not self.first:
                    self.first = self.prev
                # The second node is always the current node in a violation
                # If there are two violations, this gets updated to the latter one
                self.second = node
            
            # Move prev to current node
            self.prev = node

            inorder(node.right)

        inorder(root)
        
        # Swap the values of the two identified nodes
        if self.first and self.second:
            self.first.val, self.second.val = self.second.val, self.first.val