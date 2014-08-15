class Solution:
    # @return a list of lists of integer
    def generateMatrix(self, n):
        def circle(i,j,n):
            return min(i,j,n-1-i,n-1-j)
        def offset(k,n):
            cnt = 0
            for i in xrange(k):
                cnt += 4*(n-2*i)-4
            return cnt
        def get(i,j,n):
            m = circle(i,j,n)
            off = offset(m,n)
            dx,dy = i-m,j-m
            if not dx:
                return off + dy + 1
            if not dy:
                return off + 4*(n-2*m) - 3 - dx
            if j == n-1-m:
                return off + n-2*m + dx
            return off+ 3*(n-2*m)-2-dy
        result = [[0]*n for i in xrange(n)]
        for i in xrange(n):
            for j in xrange(n):
                result[i][j]=get(i,j,n)
        return result
