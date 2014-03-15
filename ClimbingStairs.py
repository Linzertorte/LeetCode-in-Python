class Solution:
    # @param n, an integer
    # @return an integer
    def climbStairs(self, n):
        a,b=1,1
        for i in xrange(2,n+1):
            a,b=b,a+b
        return b
