class Solution(object):
    def recoverTree(self, root):
        bad = []
        def dfs(root): #return min,max
            l,r = root,root
            if root.left:
                lmin,lmax = dfs(root.left)
                l = lmin
                if root.val<lmax.val: bad.append((lmax,root))
            if root.right:
                rmin,rmax = dfs(root.right)
                r = rmax
                if rmin.val<root.val:
                    bad.append((root,rmin))
            return l,r
        dfs(root)
        if len(bad) ==1:
            x,y = bad[0]
        else:
            ((a,b),(c,d)) = bad
            x = a if a.val>c.val else c
            y = b if b.val<d.val else d
        x.val,y.val = y.val,x.val
