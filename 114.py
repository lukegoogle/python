from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """Flattens a binary tree into a right-skewed linked list in-place.
        
        The flattening follows a preorder traversal sequence.
        
        Args:
            root: The root of the binary tree to flatten.
        """
        # prev tracks the node that will be the 'next' in the flattened list
        self.prev = None

        def traverse(node: Optional[TreeNode]):
            """Recursive helper using reverse postorder traversal.
            
            Args:
                node: Current node being processed.
            """
            if not node:
                return
            
            # 1. Visit Right first
            traverse(node.right)
            # 2. Visit Left second
            traverse(node.left)
            
            # 3. Process the current node
            # Point this node's right to the previously processed node
            node.right = self.prev
            # Set left to None as per the linked list requirement
            node.left = None
            # Current node becomes the 'prev' for the next step up the stack
            self.prev = node

        traverse(root)