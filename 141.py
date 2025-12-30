from typing import Optional

class ListNode:
    """Definition for singly-linked list node."""
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """Determines if a linked list has a cycle.

        Args:
            head: The head of the singly-linked list.

        Returns:
            True if there is a cycle, False otherwise.
        """
        if not head or not head.next:
            return False

        slow = head
        fast = head

        # Fast pointer moves twice as fast as slow pointer
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            # If they meet, there is a cycle
            if slow == fast:
                return True

        # If fast reaches the end, there is no cycle
        return False