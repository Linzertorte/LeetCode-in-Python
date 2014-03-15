# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        if head is None or head.next is None:
            return head
        if head.val == head.next.val:
            return self.deleteDuplicates(head.next)
        else:
            head.next=self.deleteDuplicates(head.next)
            return head
