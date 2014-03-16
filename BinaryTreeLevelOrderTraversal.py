# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def getNextLevel(self,level):
        next=[]
        for node in level:
            if node.left:
                next.append(node.left)
            if node.right:
                next.append(node.right)
        return next
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrder(self, root):
        levels=[]
        if not root:
            return levels
        level=[root]
        while len(level)!=0:
            levels.append(map((lambda x:x.val),level))
            level=self.getNextLevel(level)
        return levels
