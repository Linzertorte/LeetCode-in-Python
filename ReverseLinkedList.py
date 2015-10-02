class Solution(object):
    def reverseList(self, head):
        if not head: return head
        p,q,r = None,None,head
        while r:
            if q: q.next = p
            p,q,r = q,r,r.next
            if not r: break
        q.next = p
        return q
