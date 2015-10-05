class Solution(object):
    def findPeakElement(self, nums):
        n = len(nums)
        l,r = -1,n-1
        while l+1<r:
            mid = (l+r)/2
            if nums[mid]>nums[mid+1]: r=mid
            else: l=mid
        return r
