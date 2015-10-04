class Solution(object):
    def largestNumber(self, nums):
        nums = map(str,nums)
        def cmp(x,y):
            return x+y>y+x
        def mergeSort(nums):
            n = len(nums)
            if n<=1: return nums
            mid = n/2
            left = mergeSort(nums[:mid])
            right = mergeSort(nums[mid:])
            i,j,n,m = 0,0,len(left),len(right)
            x = []
            while i<n and j<m:
                if cmp(left[i],right[j]):
                    x.append(left[i])
                    i+=1
                else:
                    x.append(right[j])
                    j+=1
            while i<n:
                x.append(left[i])
                i+=1
            while j<m:
                x.append(right[j])
                j+=1
            return x
        x =  ''.join(mergeSort(nums))
        while len(x)>1 and x[0]=='0': x=x[1:]
        return x
