from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """Constructs a binary tree from preorder and inorder traversals.

        Args:
            preorder: List of node values from preorder traversal.
            inorder: List of node values from inorder traversal.

        Returns:
            The root node of the constructed binary tree.
        """
        # Map value to its index in inorder traversal for O(1) lookup
        inorder_map = {val: i for i, val in enumerate(inorder)}
        
        # Pointer to track the current root in the preorder list
        self.pre_idx = 0

        def array_to_tree(left: int, right: int) -> Optional[TreeNode]:
            """Recursive helper to build subtrees.

            Args:
                left: The left boundary of the current subtree in the inorder array.
                right: The right boundary of the current subtree in the inorder array.

            Returns:
                A TreeNode representing the root of the current subtree.
            """
            # If there are no elements to construct the tree
            if left > right:
                return None

            # Select the pre_idx element as the root and increment it
            root_val = preorder[self.pre_idx]
            root = TreeNode(root_val)
            self.pre_idx += 1

            # Root splits inorder list into left and right subtrees
            index = inorder_map[root_val]

            # Build left and right subtrees
            # Crucial: Build LEFT first because preorder is Root -> Left -> Right
            root.left = array_to_tree(left, index - 1)
            root.right = array_to_tree(index + 1, right)

            return root

        return array_to_tree(0, len(inorder) - 1)