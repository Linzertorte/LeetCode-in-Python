# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        if not head:
            return False
        if not head.next:
            return False
        turtle=head.next
        rabbit=head.next.next
        while turtle and rabbit:
            if turtle == rabbit:
                return True
            turtle=turtle.next
            if not rabbit.next:
                return False
            rabbit=rabbit.next.next
        return False
