from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """Removes duplicates from a sorted linked list such that each element appears once.

        Args:
            head: The head of a sorted singly-linked list.

        Returns:
            The head of the linked list after removing duplicate nodes.
        """
        current = head
        
        while current and current.next:
            if current.val == current.next.val:
                # Found a duplicate, skip the next node
                current.next = current.next.next
            else:
                # No duplicate, move to the next distinct element
                current = current.next
                
        return head