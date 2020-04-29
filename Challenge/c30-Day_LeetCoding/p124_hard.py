# 124. Binary Tree Maximum Path Sum
# https://leetcode.com/problems/binary-tree-maximum-path-sum/


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    # 參考答案
    def maxPathSum(self, root):
        self.res = root.val
        self.dfs(root)
        return self.res

    def dfs(self, n):
        l = self.dfs(n.left) if n.left else 0
        r = self.dfs(n.right) if n.right else 0
        m = max(n.val, l + n.val, r + n.val)
        self.res = max(self.res, m, l + r + n.val)
        return m


# class Solution(object):
#     # 參考答案
#     def maxPathSum(self, root):
#         """
#         :type root: TreeNode
#         :rtype: int
#         """
#         if root is None:
#             return 0
        
#         if root.left is None and root.right is None:
#             return root.val
        
#         res = [root.val]
#         self.maxPathSumUtil(root, res)
#         return res[0]

#     def maxPathSumUtil(self, root, res):
#         if root is None:
#             return 0
        
#         if root.left is None and root.right is None:
#             return root.val
        
#         ls = self.maxPathSumUtil(root.left, res)
#         rs = self.maxPathSumUtil(root.right, res)
    
#         if root.left is not None and root.right is not None:
#             res[0] = max(res[0], ls + rs + root.val)
#             return max(ls, rs) + root.val
        
#         if root.left is None:
#             res[0] = max(res[0], rs + root.val)
#             return rs + root.val
#         else:
#             res[0] = max(res[0], ls + root.val)
#             return ls + root.val


if __name__ == "__main__":
    

[1,2,3]
[-10,9,20,null,null,15,7]
[0]
[1,2]
[3,null,4]
[2,-1]
[-2,1]
