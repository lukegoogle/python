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
        """Populates next right pointers in any binary tree.

        Args:
            root: The root of the binary tree.

        Returns:
            The root of the tree with populated next pointers.
        """
        if not root:
            return None
        
        # Start with the root
        curr_parent = root
        
        while curr_parent:
            # Dummy node to track the head of the next level
            dummy = Node(0)
            # Pointer to build the linked list of the next level
            prev_child = dummy
            
            # Traverse the current level using 'next' pointers
            while curr_parent:
                if curr_parent.left:
                    prev_child.next = curr_parent.left
                    prev_child = prev_child.next
                if curr_parent.right:
                    prev_child.next = curr_parent.right
                    prev_child = prev_child.next
                
                # Move to the next node in the current level
                curr_parent = curr_parent.next
            
            # Move down to the start of the next level
            curr_parent = dummy.next
            
        return root