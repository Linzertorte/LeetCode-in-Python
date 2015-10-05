class Solution(object):
    def findKthLargest(self, nums, k):
        n = len(nums)
        def quick(nums,k):
            pivot,rest = nums[0], nums[1:]
            x = filter(lambda x:x<=pivot,rest)
            y = filter(lambda x:x>pivot,rest)
            if len(x)>=k: return quick(x,k)
            elif len(x)+1==k: return pivot
            else: return quick(y,k-len(x)-1)
        return quick(nums,n-k+1)
