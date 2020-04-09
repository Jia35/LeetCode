# 876. Middle of the Linked List
# https://leetcode.com/problems/middle-of-the-linked-list/


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# def printList(node):
#     while node:
#         print(node.val)
#         node = node.next


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        count = 0
        _head = head
        while head.next is not None:
            head = head.next
            count += 1
            if count % 2 == 1:
                _head = _head.next
        return _head


if __name__ == "__main__":
    node1 = ListNode(0)
    node2 = ListNode(1)
    node3 = ListNode(2)
    node4 = ListNode(3)
    node5 = ListNode(4)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    # printList(node1)

    solution = Solution()
    print(solution.middleNode(node1).val)

    # [1,2,3,4,5]
    # [1,2,3,4,5,6]
