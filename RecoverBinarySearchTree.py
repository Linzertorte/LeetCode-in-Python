class Solution(object):
    def recoverTree(self, root):
        x,y = [],[]
        def dfs(root):
            l,r = root,root
            if len(x)==2: return l,r
            if root.left:
                lmin,lmax = dfs(root.left)
                l = lmin
                if root.val<lmax.val:
                    x.append(lmax)
                    y.append(root)
            if root.right:
                rmin,rmax = dfs(root.right)
                r = rmax
                if rmin.val<root.val:
                    x.append(root)
                    y.append(rmin)
            return l,r
        dfs(root)
        x = max(x,key=lambda x:x.val)
        y = min(y,key=lambda y:y.val)
        x.val,y.val = y.val,x.val
