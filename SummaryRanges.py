class Solution(object):
    def summaryRanges(self, nums):
        def dfs(nums):
            if len(nums)==0: return (None,[])
            x,nums = nums[0],nums[1:]
            h,rest = dfs(nums)
            #print h,rest
            if h is None: return (x,[str(x)])
            if x+1==h:
                if '->' in rest[0]: return (x,[str(x)+rest[0][rest[0].index("->"):]]+rest[1:])
                else: return (x,[str(x)+'->'+rest[0]]+rest[1:])
            else: return (x,[str(x)]+rest)
        return dfs(nums)[1]
