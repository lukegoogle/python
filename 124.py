from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """Calculates the maximum path sum of any path in the binary tree.

        Args:
            root: The root node of the binary tree.

        Returns:
            The maximum path sum found.
        """
        # Initialize with a very small number
        self.max_sum = float('-inf')

        def get_max_gain(node: Optional[TreeNode]) -> int:
            """Calculates the maximum gain a node can contribute to its parent.

            Args:
                node: The current node being processed.

            Returns:
                The maximum sum of a path starting at this node and moving down.
            """
            if not node:
                return 0
            
            # Step 1: Recursively get max gains from subtrees.
            # If a gain is negative, we ignore it by taking max(0, gain).
            left_gain = max(get_max_gain(node.left), 0)
            right_gain = max(get_max_gain(node.right), 0)
            
            # Step 2: Calculate the price of a new path with the current node 
            # as the highest point (the 'apex' of the arch).
            current_path_sum = node.val + left_gain + right_gain
            
            # Step 3: Update the global maximum if the current path is better.
            self.max_sum = max(self.max_sum, current_path_sum)
            
            # Step 4: Return the maximum gain this node can contribute 
            # to its parent (only one branch can be chosen).
            return node.val + max(left_gain, right_gain)

        get_max_gain(root)
        return self.max_sum