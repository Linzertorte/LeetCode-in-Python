class Solution(object):
    def isScramble(self, s1, s2):
        dp, n, m = {}, len(s1), len(s2)
        def hist(s):
            x = [0]*26
            for c in s:
                x[ord(c)-ord('a')] += 1
            return x
        def dfs(i,j,k,l):
            if s1[i:j]==s2[k:l]: return True
            if hist(s1[i:j]) != hist(s2[k:l]):
                dp[i,j,k,l] = False
                return False
            if j-i!=l-k: return False
            if j-i==1: return False
            if (i,j,k,l) not in dp:
                dp[i,j,k,l] = False
                for p in xrange(1,j-i):
                    if dfs(i,i+p,k,k+p) and dfs(i+p,j,k+p,l): dp[i,j,k,l] = True
                    elif dfs(i,j-p,k+p,l) and dfs(j-p,j,k,k+p): dp[i,j,k,l] = True
                    elif dfs(i,i+p,l-p,l) and dfs(i+p,j,k,l-p): dp[i,j,k,l] = True
            return dp[i,j,k,l]
        return dfs(0,n,0,m)
