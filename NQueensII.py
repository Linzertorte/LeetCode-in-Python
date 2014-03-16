
class Solution:
    # @return an integer
    def no_attack(self,config,i):
        for j in xrange(i):
            if abs(j-i)==abs(config[j]-config[i]):
                return False
        return True
    def dfs(self,i,n,config,V):
        if i==n:
            return 1
        total=0
        for j in xrange(n):
            if j not in V:
                config[i]=j
                if self.no_attack(config,i):
                    V.add(j)
                    total+=self.dfs(i+1,n,config,V)
                    V.remove(j)
        return total
        
    def totalNQueens(self, n):
        config=[-1]*n
        V=set()
        return self.dfs(0,n,config,V)
