# Definition for singly-linked list with a random pointer.
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    p = dict()
    def copyRandomList(self, head):
        if head is None:
            return None
        if head not in self.p:
            node = RandomListNode(head.label)
            self.p[head] = node
            if head.next:
                node.next = self.copyRandomList(head.next)
            if head.random:
                node.random = self.copyRandomList(head.random)
        return self.p[head]
