from typing import Optional

class Node:
    """Definition for a Node."""
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        """Creates a deep copy of a linked list with random pointers.

        Args:
            head: The head of the original linked list.

        Returns:
            The head of the newly cloned linked list.
        """
        if not head:
            return None

        # Step 1: Create copied nodes and weave them into the original list
        # Original: A -> B -> C
        # Result: A -> A' -> B -> B' -> C -> C'
        curr = head
        while curr:
            new_node = Node(curr.val, curr.next)
            curr.next = new_node
            curr = new_node.next

        # Step 2: Assign random pointers for the copied nodes
        curr = head
        while curr:
            if curr.random:
                # The copy's random should point to the original's random's copy
                curr.next.random = curr.random.next
            curr = curr.next.next

        # Step 3: Separate the woven list into original and copy
        curr = head
        dummy = Node(0)
        copy_curr = dummy
        
        while curr:
            # Extract the copy
            copy_curr.next = curr.next
            copy_curr = copy_curr.next
            
            # Restore the original list
            curr.next = curr.next.next
            curr = curr.next

        return dummy.next