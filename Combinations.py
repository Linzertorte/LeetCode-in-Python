class Solution(object):
    def combine(self, n, k):
        def dfs(i,k):
            if i==n+1:
                return [[]] if k==0 else []
            if k==0: return [[]]
            return [[j]+p for j in xrange(i,n+1) for p in dfs(j+1,k-1)]
        return dfs(1,k)
