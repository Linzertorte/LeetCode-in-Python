class Solution(object):
    def subsets(self, nums):
        nums = sorted(nums)
        n = len(nums)
        def dfs(i):
            if i==n: return [[]]
            return [x+p for p in dfs(i+1) for x in [[nums[i]],[]]]
        return dfs(0)
