class Solution(object):
    def isIsomorphic(self, s, t):
        s,t = list(s),list(t)
        n,m = len(s),len(t)
        if n!=m: return False
        dp = {}
        for i in xrange(n):
            k,v=s[i],t[i]
            if k in dp:
                if dp[k]!=v: return False
            dp[k] = v
        dp = {}
        for i in xrange(n):
            v,k=s[i],t[i]
            if k in dp:
                if dp[k]!=v: return False
            dp[k] = v
        return True
