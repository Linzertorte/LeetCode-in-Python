class Solution(object):
    def kthSmallest(self, root, k):
        def kth(r,k): #return (kth,size)
            if not r: return None,0
            lk,ls = kth(r.left,k)
            if lk is not None: return lk,0
            if ls+1==k:
                return r.val,0
            if k>ls+1:
                rk,rs = kth(r.right,k-ls-1)
                if rk is not None: return rk,0
                return None,ls+rs+1
        return kth(root,k)[0]
