class Solution:
    # @param height, a list of integer
    # @return an integer
    def largestRectangleArea(self, height):
        n = len(height)
        if n==0:
            return 0
        left = [i for i in xrange(n)]
        right = [i for i in xrange(n)]
        for i in xrange(1,n):
            l = left[i]
            while l>0 and height[i]<=height[l-1]:
                l = left[l-1]
            left[i]=l
        for i in xrange(n-2,-1,-1):
            r = right[i]
            while r+1<n and height[i]<=height[r+1]:
                r = right[r+1]
            right[i] = r

        return max(map(lambda i:(right[i]-left[i]+1)*height[i],[i for i in xrange(n)]))
