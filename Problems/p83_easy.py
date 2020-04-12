# 83. Remove Duplicates from Sorted List
# https://leetcode.com/problems/remove-duplicates-from-sorted-list/


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def show(list_node: ListNode):
    while list_node:
        print(list_node.val)
        list_node = list_node.next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        s_node = ListNode(head.val)
        next_node = s_node
        pre_val = s_node.val
        
        while head:
            if head.val != pre_val:
                next_node.next = ListNode(head.val)
                next_node = next_node.next
                pre_val = head.val
            
            head = head.next

        return s_node


if __name__ == "__main__":
    solution = Solution()

    node11 = ListNode(1)
    node12 = ListNode(2)
    node13 = ListNode(2)
    node14 = ListNode(3)
    node15 = ListNode(3)
    node11.next = node12
    node12.next = node13
    node13.next = node14
    node14.next = node15

    show(solution.deleteDuplicates(node11))
