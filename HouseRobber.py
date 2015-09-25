class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = [0,0]+nums
        dp = [0]*len(nums)
        for i in xrange(2,len(nums)):
            dp[i] = max(dp[i-1],dp[i-2]+nums[i])
        return dp[-1]
