class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxSubArray(self, A):
        m = -float('inf')
        sum = 0
        for i in A:
            sum += i
            m = max(m,sum)
            if sum<0:
                sum =0
        return m
