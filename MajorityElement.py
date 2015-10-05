class Solution(object):
    def majorityElement(self, nums):
        idx,cnt = 0,1
        for i in xrange(1,len(nums)):
            if nums[i]==nums[idx]: cnt+=1
            else: cnt-=1
            if cnt==0: idx,cnt = i,1
        return nums[idx]    
