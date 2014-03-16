# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head, last=None):
        if not head:
            return None
        if last is not None and (head.val==last):
            return self.deleteDuplicates(head.next,last)
        else:
            if not head.next:
                return head
            if head.val==head.next.val:
                return self.deleteDuplicates(head.next,head.val)
            else:
                head.next=self.deleteDuplicates(head.next)
                return head
            
