class Solution(object):
    def productExceptSelf(self, nums):
        n = len(nums)
        left,right = [1]*n,[1]*n
        for i in xrange(1,n):
            left[i] = left[i-1]*nums[i-1]
        for i in xrange(n-2,-1,-1):
            right[i] = right[i+1]*nums[i+1]
        return [ left[i]*right[i] for i in xrange(n)]
