from typing import List, Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        """Performs a bottom-up level order traversal of a binary tree.

        Args:
            root: The root node of the binary tree.

        Returns:
            A list of lists, where each inner list contains node values 
            at that specific level, ordered from leaf level to root.
        """
        if not root:
            return []

        # Use a deque for the final result to prepend levels efficiently
        result = deque()
        queue = deque([root])

        while queue:
            level_size = len(queue)
            current_level = []
            
            for _ in range(level_size):
                node = queue.popleft()
                current_level.append(node.val)
                
                # Add children to the queue for the next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # Prepend the current level to the result to get bottom-up order
            result.appendleft(current_level)

        return list(result)