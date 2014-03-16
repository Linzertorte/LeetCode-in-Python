# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        if not root:
            return
        self.connect(root.left)
        self.connect(root.right)
        left=root.left
        right=root.right
        while left and right:
            last=left
            while last.next:
                last=last.next
            while left.left is None and left.right is None:
                left=left.next
                if not left:
                    last.next=right
                    return
            last.next=right
            if left.left:
                left=left.left
            else:
                left=left.right
            while right.left is None and right.right is None:
                right=right.next
                if not right:
                    return
            if right.left:
                right=right.left
            else:
                right=right.right
        
