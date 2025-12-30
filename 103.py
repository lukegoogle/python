from typing import List, Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """Performs a zigzag level order traversal of a binary tree.

        Args:
            root: The root node of the binary tree.

        Returns:
            A list of lists containing node values in zigzag order.
        """
        if not root:
            return []

        result = []
        queue = deque([root])
        # flag to track the direction of the current level
        left_to_right = True

        while queue:
            level_size = len(queue)
            # Use a deque for the current level to allow efficient prepending
            current_level = deque()
            
            for _ in range(level_size):
                node = queue.popleft()
                
                if left_to_right:
                    current_level.append(node.val)
                else:
                    current_level.appendleft(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # Convert deque to list and add to result
            result.append(list(current_level))
            # Toggle the direction for the next level
            left_to_right = not left_to_right
            
        return result