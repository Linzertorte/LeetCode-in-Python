# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @return a ListNode
    def add_help(self,l1,l2,carry=0):
        if l1 is None and l2 is None:
            if carry!=0:
                return ListNode(carry)
            else: return None
        if l1 is None:
            a=ListNode((l2.val+carry)%10)
            a.next=self.add_help(None,l2.next,(l2.val+carry)/10)
            return a
        if l2 is None:
            a=ListNode((l1.val+carry)%10)
            a.next=self.add_help(l1.next,None,(l1.val+carry)/10)
            return a
        a=ListNode((l1.val+l2.val+carry)%10)
        a.next=self.add_help(l1.next,l2.next,(l1.val+l2.val+carry)/10)
        return a
            
    def addTwoNumbers(self, l1, l2):
        return self.add_help(l1,l2)
