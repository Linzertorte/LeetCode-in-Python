class Solution:
    # @return a boolean
    def isInterleave(self, s1, s2, s3):
        n,m=len(s1),len(s2)
        if n+m != len(s3):
            return False
        dp=[[None]*(m+1) for x in xrange(n+1)]
        dp[0][0]=True
        for i in xrange(0,n+1):
            for j in xrange(0,m+1):
                if not i and not j:
                    continue
                dp[i][j]= i!=0 and s1[i-1]==s3[i+j-1] and dp[i-1][j] or\
                            j!=0 and s2[j-1]==s3[i+j-1] and dp[i][j-1]
        return dp[n][m]
