class Solution(object):
    def fourSum(self, nums, target):
        nums = sorted(nums)
        dp,n =  {}, len(nums)
        cnt = {}
        for x in nums:
            if x not in cnt: cnt[x] = 0
            cnt[x] += 1
        for i in xrange(n):
            if i!=0 and nums[i]==nums[i-1]: continue
            for j in xrange(i+1,n):
                if j!=i+1 and nums[j]==nums[j-1]: continue
                x = nums[i]+nums[j]
                if x not in dp: dp[x] = []
                dp[x].append((nums[i],nums[j]))
        answer = []
        for (k,v) in dp.iteritems():
            if target-k not in dp: continue
            w = dp[target-k]
            answer += [ (a,b,c,d) for a,b in v for c,d in w if b<c or (a==b and b==c and c==d and cnt[a]>=4) or (a<d and b==c and cnt[b]>=(2+(1 if a==b or c==d else 0)))]
        return answer
