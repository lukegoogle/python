import heapq
from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
    # We need to define comparison for the heap to handle cases 
    # where two nodes have the same value.
    def __lt__(self, other):
        return self.val < other.val

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """Merges k sorted linked lists into one sorted linked list.

        Uses a min-priority queue (heap) to efficiently find the smallest
        node among the heads of all remaining lists.

        Args:
            lists: A list of the heads of k sorted linked lists.

        Returns:
            The head of the merged sorted linked list.
        """
        heap = []
        
        # Initial: Push the head of each list into the heap
        for i, node in enumerate(lists):
            if node:
                # We store a tuple: (value, index, node)
                # The index 'i' acts as a tie-breaker so the heap doesn't 
                # try to compare ListNode objects directly if values are equal.
                heapq.heappush(heap, (node.val, i, node))
        
        dummy = ListNode(0)
        curr = dummy
        
        while heap:
            val, i, node = heapq.heappop(heap)
            
            # Append the smallest node to our result list
            curr.next = node
            curr = curr.next
            
            # If there's a next node in the same list, push it to the heap
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))
                
        return dummy.next