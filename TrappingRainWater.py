
class Solution:
    # @param A, a list of integers
    # @return an integer
    def trap(self, A):
        left=[0]*len(A)
        right=[0]*len(A)
        cur_max = 0
        for i in xrange(len(A)):
            left[i]=cur_max
            cur_max=max(cur_max,A[i])
        cur_max = 0
        
        for i in xrange(len(A)-1,-1,-1):
            right[i]=cur_max
            cur_max=max(cur_max,A[i])
        water = 0
        for i in xrange(len(A)):
            if min(left[i],right[i])>A[i]:
                water +=min(left[i],right[i])-A[i]
        return water
