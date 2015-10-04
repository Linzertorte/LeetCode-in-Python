class Solution(object):
    def largestNumber(self, nums):
        nums = map(str,nums)
        def cmp(x,y):
            return x+y>y+x
        def quickSort(nums):
            if len(nums)<=1: return nums
            pivot = nums[0]
            return quickSort(filter(lambda x:cmp(x,pivot), nums[1:]))+[pivot]+quickSort(filter(lambda x:not cmp(x,pivot),nums[1:]))
        x=''.join(quickSort(nums))
        while len(x)>1 and x[0]=='0': x=x[1:]
        return x
