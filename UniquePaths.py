class Solution:
    # @return an integer
    def combine(self,n,m,cache={}):
        if (n,m) in cache:
            return cache[(n,m)]
        if n==m or m==0:
            return 1
        cache[(n,m)]=self.combine(n-1,m,cache)+self.combine(n-1,m-1,cache)
        return cache[(n,m)]
        
    def uniquePaths(self, m, n):
        return self.combine(n+m-2,n-1)
