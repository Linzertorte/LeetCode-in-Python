class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        if root is None: return None
        if root==p or root==q:
            return root
        l = self.lowestCommonAncestor(root.left,p,q)
        r = self.lowestCommonAncestor(root.right,p,q)
        if l and r: return root
        if l: return l
        if r: return r
        return None
