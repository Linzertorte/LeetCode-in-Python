class Solution(object):
    def partition(self, s):
        dp,result,acc = {},[],[]
        def ok(i,j):
            if i>j: return True
            if (i,j) not in dp:
                dp[i,j] = (s[i]==s[j] and ok(i+1,j-1))
            return dp[i,j]
        result = {}
        def dfs(i):
            if i==len(s): return [[]]
            if i not in result:
                result[i] = [ [s[i:j+1]] + p for j in xrange(i,len(s)) if ok(i,j) for p in dfs(j+1)]
            return result[i]
        return dfs(0)
