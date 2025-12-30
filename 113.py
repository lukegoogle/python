from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        """Finds all root-to-leaf paths where the sum equals targetSum.

        Args:
            root: The root node of the binary tree.
            targetSum: The integer sum to search for.

        Returns:
            A list of lists, each containing a valid path of node values.
        """
        results = []
        
        def find_paths(node: Optional[TreeNode], remaining_sum: int, current_path: List[int]):
            """Recursive helper using backtracking to explore paths.

            Args:
                node: Current node in the traversal.
                remaining_sum: Target sum minus values of nodes already in current_path.
                current_path: List of node values in the current traversal branch.
            """
            if not node:
                return
            
            # Add current node to the path
            current_path.append(node.val)
            
            # Check if it's a leaf node and the sum matches
            if not node.left and not node.right and node.val == remaining_sum:
                # We must append a COPY of current_path because lists are mutable
                results.append(list(current_path))
            else:
                # Continue exploring left and right subtrees
                find_paths(node.left, remaining_sum - node.val, current_path)
                find_paths(node.right, remaining_sum - node.val, current_path)
            
            # Backtrack: remove the current node before returning to the parent
            current_path.pop()

        find_paths(root, targetSum, [])
        return results