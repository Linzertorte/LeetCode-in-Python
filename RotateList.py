# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def len(self,head):
        if head is None:
            return 0
        return 1+self.len(head.next)
    def advance(self,head,n):
        if n==1:
            return head
        return self.advance(head.next,n-1)
        
    def rotateRight(self, head, k):
        if head is None:
            return head
        n=self.len(head)
        k=k%n
        if k==0:
            return head
        mid=self.advance(head,n-k)
        last=self.advance(head,n)
        last.next=head
        head=mid.next
        mid.next=None
        return head
