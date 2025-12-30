from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        """Generates all structurally unique BSTs that store values 1 to n.

        Args:
            n: The range of values to include in the BSTs.

        Returns:
            A list of the root nodes of all unique BSTs.
        """
        if n == 0:
            return []

        def build_trees(start: int, end: int) -> List[Optional[TreeNode]]:
            """Recursive helper to build all possible BSTs for a given range.

            Args:
                start: The lower bound of the value range.
                end: The upper bound of the value range.

            Returns:
                A list of root nodes for the generated subtrees.
            """
            if start > end:
                return [None]
            
            all_trees = []
            # Iterate through each number to act as the root
            for i in range(start, end + 1):
                # Generate all possible left and right subtrees
                left_subtrees = build_trees(start, i - 1)
                right_subtrees = build_trees(i + 1, end)
                
                # Connect the root 'i' with all combinations of subtrees
                for l in left_subtrees:
                    for r in right_subtrees:
                        root = TreeNode(i)
                        root.left = l
                        root.right = r
                        all_trees.append(root)
            
            return all_trees

        return build_trees(1, n)