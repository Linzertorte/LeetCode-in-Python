class Solution:
    # @return an integer
    def minDistance(self, word1, word2):
        dp=[[0]*(len(word2)+1) for i in xrange(len(word1)+1)]
        for i in xrange(len(word1)+1):
            for j in xrange(len(word2)+1):
                if i!=0 and j!=0 and word1[i-1]==word2[j-1]:
                    dp[i][j]=dp[i-1][j-1]
                elif i!=0 and j!=0:
                    dp[i][j]=dp[i-1][j-1]+1
                elif i!=0 or j!=0:
                    dp[i][j]=100000
                if i>0:
                    dp[i][j]=min(dp[i][j],dp[i-1][j]+1)
                if j>0:
                    dp[i][j]=min(dp[i][j],dp[i][j-1]+1)
        return dp[len(word1)][len(word2)]
