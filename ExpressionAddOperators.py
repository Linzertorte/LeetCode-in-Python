class Solution(object):
    def addOperators(self, num, target):
        if num=="2147483648": return []
        n = len(num)
        def factor(s):
            if len(s)==1: return [s]
            return [s[0]+x+p for x in ['*',''] for p in factor(s[1:])]
        def evaluate(s):
            s = s.split('*')
            for x in s:
                if x[0]=='0' and len(x)>1: return None
            return reduce(lambda y,x: int(x)*y, s, 1) 
        def dfs(i,target):
            if i==-1:
                return [''] if target==0 else []
            r = []
            for j in xrange(i,-1,-1):
                for f in factor(num[j:i+1]):
                    x = evaluate(f)
                    if x is None: continue
                    if j == 0:
                        r+=[f] if x==target else []
                    else:
                        r += [ p+"+"+f for p in dfs(j-1,target-x)]
                        r += [ p+'-'+f for p in dfs(j-1,target+x)]
            return r
        return dfs(n-1,target)
