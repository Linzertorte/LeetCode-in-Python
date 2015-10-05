class Solution(object):
    def binaryTreePaths(self, root):
        def dfs(root):
            if root is None: return []
            if root.left is None and root.right is None: return [str(root.val)]
            return [str(root.val)+'->'+p for p in dfs(root.left)] + [str(root.val)+'->'+p for p in dfs(root.right)]
        return dfs(root)
