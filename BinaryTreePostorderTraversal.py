# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def postorderTraversal(self, root):
        #a config a {'node':TreeNode,'flag':0-2}
        stack=[]
        l=[]
        if root is None:
            return l
        stack.append({'node':root,'flag':0})
        while len(stack)!=0:
            if stack[-1]['flag']==0: #left child
                stack[-1]['flag']+=1
                if stack[-1]['node'].left is not None:
                    stack.append({'node':stack[-1]['node'].left,'flag':0})
            elif stack[-1]['flag']==1:
                stack[-1]['flag']+=1
                if stack[-1]['node'].right is not None:
                    stack.append({'node':stack[-1]['node'].right,'flag':0})
            else:
                l.append(stack[-1]['node'].val)
                stack.pop()
        return l
