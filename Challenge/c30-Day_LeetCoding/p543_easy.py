# 543. Diameter of Binary Tree
# https://leetcode.com/problems/diameter-of-binary-tree/


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        all_len = []

        def check_node(node: TreeNode, length: int) -> int:
            if not node.left and not node.right:
                return length
            elif node.left and not node.right:
                length += 1
                length = check_node(node.left, length)
            elif not node.left and node.right:
                length += 1
                length = check_node(node.right, length)
            elif node.left and node.right:
                length += 1
                length_l = check_node(node.left, length)
                length_r = check_node(node.right, length)
                if length_l > length_r:
                    length = length_l
                else:
                    length = length_r
            
            return length

        
        def add_len(root):
            if (not root) or (not root.left and not root.right):
                all_len.append(0)
                return
            
            length_l = length_r = 0
            root_left = root.left
            root_right = root.right
            if root_left:
                length_l = check_node(root_left, length_l) + 1
            if root_right:
                length_r = check_node(root_right, length_r) + 1
            
            length = length_l + length_r
            all_len.append(length)

            if root.left:
                add_len(root.left)
            if root.right:
                add_len(root.right)

        add_len(root)
        return max(all_len)

    # def diameterOfBinaryTree(self, root: TreeNode) -> int:
    #     self.ans = 0
        
    #     def depth(p):
    #         if not p:
    #             return 0
    #         left, right = depth(p.left), depth(p.right)
    #         self.ans = max(self.ans, left+right)
    #         return 1 + max(left, right)
            
    #     depth(root)
    #     return self.ans

if __name__ == "__main__":
    solution = Solution()
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)

    # node3.right = node4
    # node2.left = node3
    # node1.left = node2
    # print(solution.diameterOfBinaryTree(node1))

    node3.left = node4
    node1.right = node3
    node1.left = node2
    print(solution.diameterOfBinaryTree(node1))
    
    # node1.right = node2
    # print(solution.diameterOfBinaryTree(None))

    # [1,2,3,4,5]     # 3
    # [1,2,3,6,5,6,8,7,7]     # 5
    # [1,2,3,null,null,4,null,null,5]     # 4
    # [1,null,2,3,4,null,null,5]        # 3
