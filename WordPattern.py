class Solution(object):
    def wordPattern(self, pattern, words):
        pattern = list(pattern)
        words = words.split()
        n,m = len(pattern),len(words)
        if n!=m: return False
        dp = {}
        for i in xrange(n):
            k,v = pattern[i],words[i]
            if k in dp:
                if dp[k]!=v: return False
            else: dp[k] =v
        dp = {}
        for i in xrange(n):
            v,k = pattern[i],words[i]
            if k in dp:
                if dp[k]!=v: return False
            else: dp[k] =v
        return True
