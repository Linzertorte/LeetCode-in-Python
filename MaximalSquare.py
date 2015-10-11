class Solution(object):
    def maximalSquare(self, matrix):
        n = len(matrix)
        if n==0: return 0
        m = len(matrix[0])
        s = [[0]*(m+1) for i in xrange(n+1)]
        for i in xrange(1,n+1):
            for j in xrange(1,m+1):
                s[i][j] = s[i-1][j]+s[i][j-1]-s[i-1][j-1]+int(matrix[i-1][j-1])
        def square(i,j,L):
            return s[i+L-1][j+L-1]-s[i-1][j+L-1]-s[i+L-1][j-1]+s[i-1][j-1] == L*L
        def check(L):
            for i in xrange(1,n+1):
                for j in xrange(1,m+1):
                    if i+L-1<=n and j+L-1<=m and square(i,j,L): return True
            return False
        l,r = 0,max(n,m)+1
        while l+1<r:
            mid = (l+r)/2
            if check(mid): l=mid
            else: r = mid
        return l*l
