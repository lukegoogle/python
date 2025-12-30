from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """Merges two sorted linked lists into a single sorted list.

        Args:
            list1: The head of the first sorted linked list.
            list2: The head of the second sorted linked list.

        Returns:
            The head of the merged sorted linked list.
        """
        # Maintain a dummy node to easily return the head of the new list
        dummy = ListNode(-1)
        curr = dummy
        
        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
            
        # If one list is finished, append the rest of the other list
        curr.next = list1 if list1 is not None else list2
        
        return dummy.next