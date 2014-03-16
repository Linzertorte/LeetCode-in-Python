class Solution:
    def dfs(self,cur,n,k,coms,com):
        if not k:
            coms.append(com)
            return
        if cur==n:
            return
        self.dfs(cur+1,n,k-1,coms,com+[cur+1])
        self.dfs(cur+1,n,k,coms,com+[])
    # @return a list of lists of integers
    def combine(self, n, k):
        coms=[]
        self.dfs(0,n,k,coms,[])
        return coms
