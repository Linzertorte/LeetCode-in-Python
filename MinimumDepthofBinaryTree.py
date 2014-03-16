# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def minDepth(self, root):
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        res=1000000
        if root.left:
            res=min(res,1+self.minDepth(root.left))
        if root.right:
            res=min(res,1+self.minDepth(root.right))
        return res
