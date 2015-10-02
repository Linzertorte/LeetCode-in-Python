class Solution(object):
    def wordBreak(self, s, words):
        dp, n = {}, len(s)
        def dfs(i):
            if i==n:
                return ['']
            if i not in dp:
                dp[i] = [ ' '+ s[i:j+1] + w for j in xrange(i,n) if s[i:j+1] in words for w in dfs(j+1)]
            return dp[i]
        return map(lambda x:x[1:],dfs(0))
