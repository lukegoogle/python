from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """Reverses nodes of a linked list k at a time.

        Args:
            head: The head of the linked list.
            k: The size of the groups to be reversed.

        Returns:
            The head of the modified linked list.
        """
        dummy = ListNode(0, head)
        group_prev = dummy
        
        while True:
            # Find the kth node from the current group_prev
            kth = self._get_kth(group_prev, k)
            if not kth:
                break
                
            group_next = kth.next
            
            # Reverse the group
            prev, curr = kth.next, group_prev.next
            while curr != group_next:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            
            # Reconnect the reversed group with the rest of the list
            tmp = group_prev.next
            group_prev.next = kth
            group_prev = tmp
            
        return dummy.next

    def _get_kth(self, curr: Optional[ListNode], k: int) -> Optional[ListNode]:
        """Helper to find the kth node from the current position."""
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr