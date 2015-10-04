class Solution(object):
    def combinationSum(self, candidates, target):
        candidates = sorted(candidates)
        n = len(candidates)
        def dfs(i,t):
            if t==0: return [[]]
            if i==n: return []
            return [x*[candidates[i]]+p for x in xrange(0,t/candidates[i]+1) for p in dfs(i+1,t-x*candidates[i]) if*candidates[i]<=t]
        return dfs(0,target)
