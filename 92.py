from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:
        """Reverses a portion of a linked list from position left to right.

        Args:
            head: The head of the singly-linked list.
            left: The starting position (1-indexed) of the reversal.
            right: The ending position (1-indexed) of the reversal.

        Returns:
            The head of the modified linked list.
        """
        if not head or left == right:
            return head

        # Dummy node simplifies the logic if left is the first node
        dummy = ListNode(0, head)
        prev = dummy

        # 1. Move prev to the node at position (left - 1)
        for _ in range(left - 1):
            prev = prev.next

        # 2. Perform the reversal
        # 'curr' stays at the original node at 'left' position
        # Throughout the loop, 'curr' will eventually become the tail of the sublist
        curr = prev.next
        for _ in range(right - left):
            # temp is the node to be moved to the front of the sublist
            temp = curr.next
            # Bridge the gap
            curr.next = temp.next
            # Move temp to the position after prev
            temp.next = prev.next
            prev.next = temp

        return dummy.next