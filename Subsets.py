class Solution(object):
    def subsets(self, nums):
        nums = sorted(nums)
        n = len(nums)
        def dfs(i):
            if i==n: return [[]]
            return [x+p for x in [[nums[i]],[]] for p in dfs(i+1)]
        return dfs(0)
