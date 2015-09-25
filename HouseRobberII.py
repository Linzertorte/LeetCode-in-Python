class Solution(object):
    def rob_easy(self, nums):
        nums = [0,0]+nums
        dp = [0]*len(nums)
        for i in xrange(2,len(nums)):
            dp[i] = max(dp[i-1],dp[i-2]+nums[i])
        return dp[-1]
    def rob(self, nums):
        if len(nums)==0:
            return 0
        if len(nums)<=2:
            return max(nums)
        return max(self.rob_easy(nums[1:]), nums[0]+self.rob_easy(nums[2:-1]))
