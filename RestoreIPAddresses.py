class Solution(object):
    def restoreIpAddresses(self, s):
        def ok(s):
            return s=="0" or s[0]!='0' and int(s)<256
        def dfs(s,n):
            if s=="":
                return [""] if n==0 else []
            if n==0: return []
            return [ '.'+s[:i]+p for i in xrange(1,4) for p in dfs(s[i:],n-1) if i<=len(s) and ok(s[:i])]
        return map(lambda x:x[1:], dfs(s,4))
