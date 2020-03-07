# 203. Remove Linked List Elements
# https://leetcode.com/problems/remove-linked-list-elements/
from typing import List


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if head is None:
            return head
        while head.val == val:
            head = head.next
            if head is None:
                return head
        a = ListNode(head.val)
        head = head.next
        b = a
        
        while head is not None:
            if head.val != val:
                b.next = ListNode(head.val)
                b = b.next
            head = head.next

        return a


if __name__ == "__main__":
    solution = Solution()
    
