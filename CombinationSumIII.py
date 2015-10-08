class Solution(object):
    def combinationSum3(self, k, n):
        def dfs(k,n,i):
            if k==0:
                return [[]] if n==0 else []
            if i==0 or n==0: return []
            return [p+[j] for j in xrange(1,i+1) if n-j>=0 for p in dfs(k-1,n-j,j-1)]
        return dfs(k,n,9)
