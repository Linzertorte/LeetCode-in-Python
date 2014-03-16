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
    def level_rec(self,level,levels):
        if len(level)==0:
            return
        next=self.getNextLevel(level)
        self.level_rec(next,levels)
        levels.append(map((lambda x:x.val),level))
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrderBottom(self, root):
        levels=[]
        if not root:
            return levels
        level=[root]
        self.level_rec(level,levels)
        return levels
