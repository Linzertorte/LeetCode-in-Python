# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return nothing
    def len(self,head):
        cnt = 0
        p=head
        while p:
            cnt+=1
            p=p.next
        return cnt
    def advance(self,head,n):
        p=head
        for x in xrange(1,n):
            p=p.next
        return p
        
    def reverse(self,head):
        if not head:
            return head
        next=head.next
        head.next=None
        while next:
            nnext=next.next
            next.next=head
            head=next
            next=nnext
        return head
    def interleave(self,l0,l1):
        if not l0: return l1
        if not l1: return l0
        head=l0
        p0,p1=l0.next,l1.next
        head.next=l1
        p=l1
        while p0 and p1:
            p00,p11=p0.next,p1.next
            p.next=p0
            p0.next=p1
            p=p1
            p0,p1=p00,p11
        if not p0: p.next=p1
        if not p1: p.next=p0
        return head
    def reorderList(self, head):
        if head is None:
            return
        n=self.len(head)
        mid=self.advance(head,n-n/2)
        l0=head
        l1=self.reverse(mid.next)
        mid.next=None
        head=self.interleave(l0,l1)
        
        
