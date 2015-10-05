class Solution(object):
    def wordPattern(self, pattern, words):
        pattern = list(pattern)
        words = words.split()
        n,m = len(pattern),len(words)
        if n!=m: return False
        dp1,dp2 = {},{}
        for i in xrange(n):
            k,v = pattern[i],words[i]
            if k in dp1:
                if dp1[k]!=v: return False
            else: dp1[k] =v
            if v in dp2:
                if dp2[v]!=k: return False
            else: dp2[v]=k
        return True
