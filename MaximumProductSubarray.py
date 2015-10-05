class Solution(object):
    def maxProduct(self, nums):
        x,y = nums[0],nums[0]
        best = y
        for n in nums[1:]:
            x,y = min(n*x,n*y,n),max(n*x,n*y,n)
            best = max(y,best)
        return best
