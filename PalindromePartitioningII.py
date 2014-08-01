class Solution:
    # @param s, a string
    # @return an integer
    def minCut(self, s):
        n = len(s)
        yes = [[0]*(n+1) for i in xrange(n+1)]
        for i in xrange(n):
            yes[i][i] = yes[i][i+1] = 1
        for k in xrange(2,n+1):
            for i in xrange(n):
                j = i+k
                if j>n:
                    continue
                if s[i]==s[j-1] and yes[i+1][j-1]:
                    yes[i][j] = 1
        dp = [float('inf')]*n
        dp[0] = 1
        for i in xrange(1,n):
            for j in xrange(i,-1,-1):
                if yes[j][i+1]==1:
                    if j==0:
                        dp[i] = min(dp[i],1)
                    else:
                        dp[i] = min(dp[i],dp[j-1]+1)
        return dp[n-1]-1
