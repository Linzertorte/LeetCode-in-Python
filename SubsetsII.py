class Solution(object):
    def subsetsWithDup(self, nums):
        n = len(nums)
        nums = sorted(nums)
        x = [0]+filter(lambda i:nums[i]!=nums[i-1], range(1,n))+[n]
        n = len(x)-1
        def subsets(i):
            if i==n: return [[]]
            cnt = x[i+1]-x[i]
            num = nums[x[i]]
            return [[num]*t+p for t in xrange(0,cnt+1) for p in subsets(i+1)]
        return subsets(0)
