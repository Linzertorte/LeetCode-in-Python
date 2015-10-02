
class Solution(object):
    def reverseList(self, head):
        if not head: return head
        p,q,r = None,None,head
        for i in xrange(2):
            if q: q.next = p
            p,q,r = q,r,r.next
            if not r: break
        while r:
            q.next = p
            p,q,r = q,r,r.next
        q.next = p
        return q
