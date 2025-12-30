from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """Swaps every two adjacent nodes in a linked list.

        Args:
            head: The head of the singly-linked list.

        Returns:
            The head of the linked list after swapping pairs.
        """
        # Create a dummy node to point to the head
        dummy = ListNode(0)
        dummy.next = head
        prev_node = dummy
        
        while head and head.next:
            # Nodes to be swapped
            first_node = head
            second_node = head.next
            
            # Swapping logic
            prev_node.next = second_node
            first_node.next = second_node.next
            second_node.next = first_node
            
            # Reinitializing pointers for the next iteration
            prev_node = first_node
            head = first_node.next
            
        return dummy.next