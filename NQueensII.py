
class Solution:
    # @return an integer
    def no_attack(self,config,i):
        for j in xrange(i):
            if abs(j-i)==abs(config[j]-config[i]) or\
            config[i]==config[j]:
                return False
        return True
    def dfs(self,i,n,config):
        if i==n:
            return 1
        total=0
        for j in xrange(n):
            config[i]=j
            if self.no_attack(config,i):
                total+=self.dfs(i+1,n,config)
        return total
        
    def totalNQueens(self, n):
        config=[-1]*n
        return self.dfs(0,n,config)
