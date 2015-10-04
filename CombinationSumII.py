class Solution(object):
    def combinationSum2(self, candidates, target):
        nums = sorted(candidates)
        n = len(nums)
        d = filter(lambda i:nums[i-1]!=nums[i], range(1,n))
        d = [0]+d+[n]
        n = len(d)-1
        # cnt d[i+1]-d[i]
        # x nums[d[i]]
        def dfs(i,t):
            if t==0: return [[]]
            if i==n: return []
            ans,x = [], nums[d[i]]
            for j in xrange(0,d[i+1]-d[i]+1):
                if j*x>t: break
                ans += [ [x]*j+p for p in dfs(i+1,t-j*x)]
            return ans
        return dfs(0,target)
