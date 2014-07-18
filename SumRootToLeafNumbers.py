# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    sum = 0
    def sumNumbers(self, root):
        def dfs(root,sofar):
            if root.left is None and root.right is None:
                self.sum += int(''.join(map(str,sofar+[root.val])))
                return
            if root.left is not None:
                dfs(root.left,sofar+[root.val])
            if root.right is not None:
                dfs(root.right,sofar+[root.val])
        if root is None:
            return 0
        dfs(root,[])
        return self.sum
