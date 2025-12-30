from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """Performs an inorder traversal of a binary tree iteratively.

        Args:
            root: The root node of the binary tree.

        Returns:
            A list of integers representing the inorder traversal.
        """
        res = []
        stack = []
        curr = root
        
        while curr or stack:
            # 1. Reach the leftmost node of the current subtree
            while curr:
                stack.append(curr)
                curr = curr.left
            
            # 2. Process the node (Root)
            curr = stack.pop()
            res.append(curr.val)
            
            # 3. Move to the right subtree
            curr = curr.right
            
        return res