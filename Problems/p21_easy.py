# 21. Merge Two Sorted Lists
# https://leetcode.com/problems/merge-two-sorted-lists/


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def show(list_node: ListNode):
    while list_node:
        print(list_node.val)
        list_node = list_node.next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # if (not l1) and (not l2):
        #     return
        # elif (l1) and (not l2):
        #     s_node = l1
        #     l1 = l1.next
        # elif (not l1) and (l2):
        #     s_node = l2
        #     l2 = l2.next
        # elif l1 and l2:
        #     if l1.val < l2.val:
        #         s_node = l1
        #         l1 = l1.next
        #     else:
        #         s_node = l2
        #         l2 = l2.next
        
        # next_node = s_node

        # while (l1 or l2):
        #     if (l1) and (not l2):
        #         next_node.next = l1
        #         l1 = l1.next
            
        #     elif (not l1) and (l2):
        #         next_node.next = l2
        #         l2 = l2.next
            
        #     elif l1 and l2:
        #         if l1.val < l2.val:
        #             next_node.next = l1
        #             l1 = l1.next
        #         else:
        #             next_node.next = l2
        #             l2 = l2.next
        #     next_node = next_node.next
        #     # print(s_node.val)
        # return s_node

        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2


if __name__ == "__main__":
    solution = Solution()

    node11 = ListNode(1)
    node12 = ListNode(2)
    node13 = ListNode(4)
    node11.next = node12
    node12.next = node13

    node21 = ListNode(1)
    node22 = ListNode(3)
    node23 = ListNode(4)
    node21.next = node22
    node22.next = node23

    show(solution.mergeTwoLists(node11, node21))
    