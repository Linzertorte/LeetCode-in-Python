# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a list node
    def detectCycle(self, head):
        if not head:
            return None
        if not head.next:
            return None
        turtle=head.next
        rabbit=head.next.next
        while turtle and rabbit:
            if turtle == rabbit:
                p=head
                while p!=turtle:
                    p,turtle=p.next,turtle.next
                return p
            turtle=turtle.next
            if not rabbit.next:
                break
            rabbit=rabbit.next.next
        return None
