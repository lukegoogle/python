from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        """Converts a sorted linked list into a height-balanced BST.

        Uses an inorder simulation approach to achieve O(n) time complexity.

        Args:
            head: The head of the sorted linked list.

        Returns:
            The root of the height-balanced BST.
        """
        # 1. Count the total number of nodes in the linked list
        size = 0
        curr = head
        while curr:
            size += 1
            curr = curr.next
            
        self.head = head

        def convert(left: int, right: int) -> Optional[TreeNode]:
            """Recursive helper to build the BST using inorder traversal.

            Args:
                left: The starting index range.
                right: The ending index range.

            Returns:
                The root node of the current subtree.
            """
            if left > right:
                return None
            
            mid = (left + right) // 2
            
            # Step A: Recursively build the left subtree
            left_subtree = convert(left, mid - 1)
            
            # Step B: Process the Root (current head of the linked list)
            root = TreeNode(self.head.val)
            root.left = left_subtree
            
            # Move the linked list pointer forward
            self.head = self.head.next
            
            # Step C: Recursively build the right subtree
            root.right = convert(mid + 1, right)
            
            return root

        return convert(0, size - 1)