class Solution(object):
    def getIntersectionNode(self, ha, hb):
        p,q = ha,hb
        while p and q:
            p,q=p.next,q.next
        if p:
            ha,hb = hb,ha
            p,q = q,p
        k = 0
        while q:
            k += 1
            q = q.next
        p,q = ha,hb
        for i in xrange(k): q=q.next
        while p and q:
            if p==q: return p
            p,q = p.next, q.next
        return None
