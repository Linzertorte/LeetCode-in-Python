class Solution:
    def dfs(self,cur,n,S,sets,one):
        if cur==n:
            sets.append(one)
            return
        self.dfs(cur+1,n,S,sets,one+[])
        self.dfs(cur+1,n,S,sets,one+[S[cur]])
    # @param S, a list of integer
    # @return a list of lists of integer
    def subsets(self, S):
        sets=[]
        self.dfs(0,len(S),sorted(S),sets,[])
        return sets
