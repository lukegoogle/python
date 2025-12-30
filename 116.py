from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: Optional['Node']) -> Optional['Node']:
        """Populates next right pointers in a perfect binary tree.

        Args:
            root: The root of the perfect binary tree.

        Returns:
            The root of the tree after next pointers are populated.
        """
        if not root:
            return None
        
        # Start with the root node. 'leftmost' tracks the start of each level.
        leftmost = root
        
        # Since it's a perfect tree, if leftmost.left exists, the next level exists.
        while leftmost.left:
            # Iterate through the current level using the 'next' pointers 
            # we established in the previous iteration.
            head = leftmost
            while head:
                # Connection type 1: Children of the same parent
                head.left.next = head.right
                
                # Connection type 2: Children of different parents
                if head.next:
                    head.right.next = head.next.left
                
                # Move to the next node in the current level
                head = head.next
            
            # Move down to the next level
            leftmost = leftmost.left
            
        return root