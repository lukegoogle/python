from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """Rotates the linked list to the right by k places.

        Args:
            head: The head node of the singly-linked list.
            k: The number of places to rotate.

        Returns:
            The new head of the rotated linked list.
        """
        if not head or not head.next or k == 0:
            return head

        # 1. Compute the length and find the old tail
        old_tail = head
        length = 1
        while old_tail.next:
            old_tail = old_tail.next
            length += 1
        
        # 2. Optimize k and handle edge case
        k = k % length
        if k == 0:
            return head
        
        # 3. Connect tail to head to form a circle
        old_tail.next = head
        
        # 4. Find the new tail: (length - k - 1) steps from the head
        new_tail = head
        for _ in range(length - k - 1):
            new_tail = new_tail.next
            
        # 5. Break the circle
        new_head = new_tail.next
        new_tail.next = None
        
        return new_head