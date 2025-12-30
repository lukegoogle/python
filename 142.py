from typing import Optional

class ListNode:
    """Definition for singly-linked list node."""
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """Finds the node where the cycle begins in a linked list.

        Args:
            head: The head of the singly-linked list.

        Returns:
            The node where the cycle begins, or None if no cycle exists.
        """
        if not head or not head.next:
            return None

        slow = head
        fast = head

        # Phase 1: Determine if a cycle exists
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                # Cycle detected! Move to Phase 2.
                break
        else:
            # If the loop finished without a break, no cycle exists
            return None

        # Phase 2: Find the entrance to the cycle
        # Reset one pointer to the head and keep the other at the meeting point
        pointer_start = head
        pointer_meeting = slow
        
        while pointer_start != pointer_meeting:
            pointer_start = pointer_start.next
            pointer_meeting = pointer_meeting.next
            
        return pointer_start