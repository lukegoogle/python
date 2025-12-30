from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """Removes all nodes that have duplicate numbers from a sorted linked list.

        Args:
            head: The head of a sorted singly-linked list.

        Returns:
            The head of the modified linked list containing only distinct numbers.
        """
        # Sentinel node to handle cases where the head needs to be removed
        dummy = ListNode(0, head)
        # 'prev' is the last node known to be part of the distinct list
        prev = dummy
        
        while head:
            # If it's a start of a duplicate sequence
            if head.next and head.val == head.next.val:
                # Move head until we reach the last node of the duplicate sequence
                while head.next and head.val == head.next.val:
                    head = head.next
                # Skip all duplicates: connect prev's next to the node after head
                prev.next = head.next
            else:
                # No duplicate detected, move prev forward
                prev = prev.next
                
            # Move head forward for the next iteration
            head = head.next
            
        return dummy.next