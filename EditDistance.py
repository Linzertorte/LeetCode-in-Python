class Solution(object):
    def minDistance(self, word1, word2):
        n,m = len(word1),len(word2)
        dp = [[0]*(m+1) for i in xrange(n+1)]
        for i in xrange(1,n+1): dp[i][0] = i
        for j in xrange(1,m+1): dp[0][j] = j
        for i in xrange(1,n+1):
            for j in xrange(1,m+1):
                dp[i][j] = dp[i-1][j-1] + (1 if word1[i-1]!=word2[j-1] else 0)
                dp[i][j] = min([dp[i][j],dp[i-1][j]+1,dp[i][j-1]+1])
        return dp[n][m]
