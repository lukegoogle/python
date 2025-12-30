from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        """Partitions a linked list around a value x.

        Nodes less than x will precede nodes greater than or equal to x while
        maintaining original relative order.

        Args:
            head: The head of the singly-linked list.
            x: The partition threshold value.

        Returns:
            The head of the partitioned linked list.
        """
        # Create dummy nodes for the two partitions
        before_dummy = ListNode(0)
        after_dummy = ListNode(0)
        
        # Pointers to manage the end of the two growing lists
        before = before_dummy
        after = after_dummy
        
        curr = head
        while curr:
            if curr.val < x:
                before.next = curr
                before = before.next
            else:
                after.next = curr
                after = after.next
            curr = curr.next
        
        # Important: Terminate the 'after' list to avoid cycles
        after.next = None
        
        # Connect the two partitions
        before.next = after_dummy.next
        
        return before_dummy.next