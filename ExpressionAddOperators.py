class Solution(object):
    def addOperators(self, num, target):
        n = len(num)
        def factor(s):
            if len(s)==0: return ['']
            n = 1 if s[0]=='0' else len(s)
            r = []
            for i in xrange(0,n):
                op = '' if i+1 ==len(s) else '*'
                r += [s[:i+1]+op+p for p in factor(s[i+1:])]
            return r
        def evaluate(s):
            s = s.split('*')
            return reduce(lambda y,x: int(x)*y, s, 1) 
        dp = {}
        def dfs(i,target):
            if i==-1:
                return [''] if target==0 else []
            if (i,target) in dp: return dp[i,target]
            r = []
            for j in xrange(i,-1,-1):
                for f in factor(num[j:i+1]):
                    x = evaluate(f)
                    if j == 0:
                        r+=[f] if x==target else []
                    else:
                        r += [ p+"+"+f for p in dfs(j-1,target-x)]
                        r += [ p+'-'+f for p in dfs(j-1,target+x)]
            dp[i,target] = r
            return r
        return dfs(n-1,target)
