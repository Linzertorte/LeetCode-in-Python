class Solution(object):
    def wordBreak(self, s, words):
        dp ={}
        def ok(s):
            if s=="": return True
            if s in dp: return dp[s]
            for i in xrange(0,len(s)):
                if s[:i+1] in words and ok(s[i+1:]):
                    dp[s] = True
                    return True
            dp[s] = False
            return False
        return ok(s)
