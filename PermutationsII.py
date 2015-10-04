class Solution(object):
    def permuteUnique(self, nums):
        def dfs(nums):
            if len(nums)==1:
                return [nums]
            
            v,n = set(), len(nums)
            x = [[nums[0]]+p for p in dfs(nums[1:])]
            v.add(nums[0])
            for i in xrange(1,n):
                if nums[i] in v: continue
                x += [ [nums[i]]+p for p in dfs(nums[1:i]+[nums[0]]+nums[i+1:])]
                v.add(nums[i])
            return x
        return dfs(nums)
