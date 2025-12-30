from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        """Calculates the total sum of all root-to-leaf numbers.

        Each path from root to leaf represents a number (e.g., 1->2 is 12).

        Args:
            root: The root of the binary tree.

        Returns:
            The sum of all numbers formed by root-to-leaf paths.
        """
        def dfs(node: Optional[TreeNode], current_sum: int) -> int:
            """Recursive helper to traverse the tree and accumulate sums.

            Args:
                node: Current node being visited.
                current_sum: The number formed by the path from root to node.

            Returns:
                The accumulated sum for the subtrees rooted at 'node'.
            """
            if not node:
                return 0
            
            # Update the current number by shifting digits left and adding current val
            current_sum = current_sum * 10 + node.val
            
            # If we reach a leaf node, return the number formed by this path
            if not node.left and not node.right:
                return current_sum
            
            # Otherwise, continue the DFS on both children and sum their results
            return dfs(node.left, current_sum) + dfs(node.right, current_sum)

        return dfs(root, 0)