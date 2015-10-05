class Solution(object):
    def removeElements(self, head, val):
        sentinal = ListNode(-1)
        sentinal.next = head
        q,p = sentinal, head
        while p:
            if p.val == val:
                q.next = p.next
            else: q = p
            p=p.next
        return sentinal.next
