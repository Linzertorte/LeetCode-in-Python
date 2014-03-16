class Solution:
    def no_attack(self,config,i):
        for j in xrange(i):
            if abs(j-i)==abs(config[j]-config[i]) or\
            config[i]==config[j]:
                return False
        return True
    def dfs(self,i,n,config,sol):
        if i==n:
            s=['']*n
            for j in xrange(n):
                s[j]='.'*config[j]+'Q'+'.'*(n-config[j]-1)
            sol.append(s)
            return
        for j in xrange(n):
            config[i]=j
            if self.no_attack(config,i):
                self.dfs(i+1,n,config,sol)
    # @return a list of lists of string
    def solveNQueens(self, n):
        sol=[]
        config=[-1]*n
        self.dfs(0,n,config,sol)
        return sol
