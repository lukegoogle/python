from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        """Constructs a binary tree from inorder and postorder traversals.

        Args:
            inorder: List of node values from inorder traversal.
            postorder: List of node values from postorder traversal.

        Returns:
            The root node of the constructed binary tree.
        """
        # Map value to its index in inorder traversal for O(1) lookup
        inorder_map = {val: i for i, val in enumerate(inorder)}
        
        # Start from the last element of postorder
        self.post_idx = len(postorder) - 1

        def array_to_tree(left: int, right: int) -> Optional[TreeNode]:
            """Recursive helper to build subtrees.

            Args:
                left: The left boundary in the inorder array.
                right: The right boundary in the inorder array.

            Returns:
                The root node of the current subtree.
            """
            if left > right:
                return None

            # Select the post_idx element as the root and decrement
            root_val = postorder[self.post_idx]
            root = TreeNode(root_val)
            self.post_idx -= 1

            # Root splits inorder list into left and right subtrees
            index = inorder_map[root_val]

            # Build RIGHT subtree before LEFT subtree
            # This is because postorder is Left -> Right -> Root
            # Moving backwards from the end, we encounter Root, then Right, then Left.
            root.right = array_to_tree(index + 1, right)
            root.left = array_to_tree(left, index - 1)

            return root

        return array_to_tree(0, len(inorder) - 1)