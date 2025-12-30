from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """Removes the nth node from the end of a linked list in one pass.

        Args:
            head: The head of the singly-linked list.
            n: The position from the end of the node to remove.

        Returns:
            The head of the modified linked list.
        """
        # Dummy node helps handle the case where we remove the head
        dummy = ListNode(0, head)
        fast = dummy
        slow = dummy
        
        # Advance fast pointer so that the gap between fast and slow is n nodes
        for _ in range(n + 1):
            fast = fast.next
            
        # Move fast to the end, maintaining the gap
        while fast is not None:
            fast = fast.next
            slow = slow.next
            
        # slow.next is the nth node from the end; skip it
        slow.next = slow.next.next
        
        return dummy.next