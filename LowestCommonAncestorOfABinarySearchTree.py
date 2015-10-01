class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        def answerAndCount(root,p,q):
            if root is None: return (None,0)
            la,lc = answerAndCount(root.left,p,q)
            ra,rc = answerAndCount(root.right,p,q)
            if la: return (la,lc)
            if ra: return (ra,rc)
            if root==p and root==q: return (root,2)
            if root==p or root==q:
                if lc==1 or rc==1: return (root,2)
                else: return (None,1)
            if lc==1 and rc==1: return (root,2)
            return (None, lc+rc)
        return answerAndCount(root,p,q)[0]
