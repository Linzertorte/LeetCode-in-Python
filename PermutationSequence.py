class Solution(object):
    def getPermutation(self, n, k):
        fact=[1]*10
        for i in xrange(1,10):
            fact[i] = i*fact[i-1]
        def dfs(n,k):
            if k==1: return [1]*n
            i=1
            while i*fact[n-1]<k: i+=1
            return [i]+dfs(n-1, k-(i-1)*fact[n-1])
        x = dfs(n,k)
        for i in xrange(1,n):
            y = filter(lambda k:k not in x[:i], range(1,n+1))
            x[i] = y[x[i]-1]
        return ''.join(map(str,x))
